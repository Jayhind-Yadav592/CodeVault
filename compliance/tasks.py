from django_q.tasks import async_task
from .models import ComplianceEvaluation, CompliancePolicy, RuleResult
from .engine import RuleContext
from .rules import ALL_RULES
from repositories.services.git_service import GitService

def run_compliance_evaluation_task(evaluation_id):
    try:
        evaluation = ComplianceEvaluation.objects.get(id=evaluation_id)
        evaluation.decision = ComplianceEvaluation.Decision.INSUFFICIENT_DATA
        evaluation.save()
        
        # Check if we need to clone
        needs_clone = any(rule.requires_file_scan for rule in ALL_RULES)
        repo_path = None
        git_service = None
        
        if needs_clone:
            connection = evaluation.snapshot.repository
            git_service = GitService(connection.repo_url, connection.default_branch)
            git_service.clone()
            repo_path = git_service.get_repo_path()
            
        context = RuleContext(evaluation, repo_path=repo_path)
        
        total_score = 0.0
        max_score = 0.0
        
        has_critical_failure = False
        
        for RuleClass in ALL_RULES:
            rule_def = RuleClass.get_or_create_model()
            if not rule_def.is_enabled:
                continue
                
            rule_instance = RuleClass()
            try:
                result_dict = rule_instance.evaluate(context)
            except Exception as e:
                result_dict = rule_instance._unknown({'error': str(e)}, 'Execution failed')
                
            status = result_dict['status']
            score = result_dict.get('score_contribution', 0.0)
            critical = result_dict.get('is_critical_failure', False)
            
            # Map category to weight
            weight = getattr(evaluation.policy, f"weight_{rule_def.category}", 10.0)
            
            if status == RuleResult.Status.PASS:
                evaluation.passed_rules += 1
                total_score += weight
                max_score += weight
            elif status == RuleResult.Status.FAIL:
                evaluation.failed_rules += 1
                max_score += weight
                if critical:
                    has_critical_failure = True
                    evaluation.critical_findings += 1
            elif status == RuleResult.Status.WARNING:
                evaluation.warnings += 1
                total_score += (weight * score)
                max_score += weight
            elif status == RuleResult.Status.UNKNOWN:
                evaluation.unknown_rules += 1
            
            RuleResult.objects.create(
                evaluation=evaluation,
                rule=rule_def,
                status=status,
                evidence=result_dict.get('evidence', {}),
                remediation=result_dict.get('remediation', ''),
                is_critical_failure=critical,
                score_contribution=score
            )
            
        if git_service:
            git_service.cleanup()
            
        if max_score > 0:
            evaluation.overall_score = (total_score / max_score) * 100
        else:
            evaluation.overall_score = 0
            
        # Decision Logic
        if has_critical_failure:
            evaluation.decision = ComplianceEvaluation.Decision.INELIGIBLE
        elif evaluation.overall_score >= 90 and evaluation.failed_rules == 0:
            evaluation.decision = ComplianceEvaluation.Decision.ELIGIBLE
        elif evaluation.overall_score >= 70:
            evaluation.decision = ComplianceEvaluation.Decision.CONDITIONALLY_ELIGIBLE
        elif evaluation.unknown_rules > 0 or evaluation.warnings > 0:
            evaluation.decision = ComplianceEvaluation.Decision.REQUIRES_HUMAN_REVIEW
        else:
            evaluation.decision = ComplianceEvaluation.Decision.INELIGIBLE
            
        evaluation.save()
        
    except Exception as e:
        print(f"Compliance evaluation failed: {e}")

def trigger_compliance_evaluation(snapshot):
    policy, _ = CompliancePolicy.objects.get_or_create(is_active=True, defaults={'version': '1.0'})
    evaluation = ComplianceEvaluation.objects.create(
        snapshot=snapshot,
        policy=policy,
        decision=ComplianceEvaluation.Decision.INSUFFICIENT_DATA
    )
    async_task('compliance.tasks.run_compliance_evaluation_task', evaluation.id)
    return evaluation
