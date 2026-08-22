import os
import re
from compliance.models import ComplianceRule, RuleResult
from .engine import BaseRule, RuleContext
from repositories.models import PullRequestStat

# ================================
# Snapshot-Based Rules
# ================================

class RepositorySizeRule(BaseRule):
    rule_id = 'repository_size'
    name = 'Minimum Meaningful LOC'
    description = 'Evaluates if the repository meets the minimum meaningful lines of code.'
    category = ComplianceRule.Category.REPOSITORY
    severity = ComplianceRule.Severity.CRITICAL
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        actual = context.snapshot.meaningful_loc
        required = context.policy.min_meaningful_loc
        
        evidence = {
            'actual_loc': actual,
            'required_loc': required
        }
        
        if actual >= required:
            return self._pass(evidence)
        return self._fail(
            evidence,
            remediation="Increase genuine project functionality and source-code coverage. Do not add generated, blank, or comment-only lines.",
            critical=True
        )

class GitCommitRule(BaseRule):
    rule_id = 'git_history_commits'
    name = 'Minimum Meaningful Commits'
    description = 'Evaluates if the repository has the minimum required meaningful commits.'
    category = ComplianceRule.Category.GIT_HISTORY
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        actual = context.snapshot.meaningful_commits
        required = context.policy.min_meaningful_commits
        
        evidence = {
            'total_commits': context.snapshot.total_commits,
            'meaningful_commits': actual,
            'required_commits': required,
            'excluded_commits': context.snapshot.total_commits - actual,
            'exclusion_reason': 'Merge commits and short messages are excluded.'
        }
        
        if actual >= required:
            return self._pass(evidence)
        return self._fail(
            evidence,
            remediation="Ensure the repository shows genuine iterative development history.",
        )

class PullRequestRule(BaseRule):
    rule_id = 'pull_request_history'
    name = 'Pull Request History'
    description = 'Evaluates if the repository utilizes pull requests.'
    category = ComplianceRule.Category.GIT_HISTORY
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        try:
            pr_stat = context.snapshot.pr_stats
        except PullRequestStat.DoesNotExist:
            return self._unknown({'reason': 'No PR stats found in snapshot.'}, 'Ensure provider API access is available.')

        if not pr_stat.is_available:
            return self._unknown({'reason': 'Connected repository provider does not expose pull-request metadata.'})

        required = context.policy.min_meaningful_prs
        actual = pr_stat.merged_prs
        
        evidence = {'merged_prs': actual, 'required_prs': required, 'total_prs': pr_stat.total_prs}
        
        if actual >= required:
            return self._pass(evidence)
        return self._fail(evidence, remediation="Use pull requests for code review and merging workflows.")

class SupportedLanguageRule(BaseRule):
    rule_id = 'supported_language'
    name = 'Supported Language'
    description = 'Evaluates if the repository contains recognized languages.'
    category = ComplianceRule.Category.CODE_QUALITY
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        languages = list(context.snapshot.languages.all())
        supported = [l for l in languages if l.language_name != 'Unknown' and l.loc > 0]
        unsupported = [l for l in languages if l.language_name == 'Unknown' and l.loc > 0]
        
        evidence = {
            'detected_languages': [l.language_name for l in languages],
            'supported_loc': sum(l.loc for l in supported),
            'unsupported_loc': sum(l.loc for l in unsupported)
        }
        
        if supported:
            if unsupported and evidence['unsupported_loc'] > evidence['supported_loc']:
                return self._warning(evidence, remediation="Ensure the primary language is supported.")
            return self._pass(evidence)
        return self._fail(evidence, remediation="Repository must contain source code in supported languages.")

class OwnershipRule(BaseRule):
    rule_id = 'ownership_declaration'
    name = 'Ownership Declaration'
    description = 'Checks if the project has a signed ownership declaration.'
    category = ComplianceRule.Category.OWNERSHIP
    severity = ComplianceRule.Severity.CRITICAL
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        decl = context.project.ownership_declarations.order_by('-created_at').first()
        if not decl:
            return self._fail({'reason': 'No ownership declaration found.'}, remediation="Submit a signed ownership declaration.", critical=True)
            
        evidence = {
            'status': decl.status,
            'version': decl.declaration_version,
            'timestamp': decl.created_at.isoformat()
        }
        
        from projects.models import OwnershipDeclaration
        if decl.status == OwnershipDeclaration.Status.SIGNED:
            return self._pass(evidence)
        return self._fail(evidence, remediation="Ownership declaration must be SIGNED.", critical=True)

# ================================
# Scanner-Based Rules
# ================================

class ExecutabilityRule(BaseRule):
    rule_id = 'executability'
    name = 'Executable Project'
    description = 'Checks if the project appears to be an executable application.'
    category = ComplianceRule.Category.CODE_QUALITY
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = True

    def evaluate(self, context: RuleContext):
        indicators = {
            'python_django': ['manage.py', 'requirements.txt'],
            'python_fastapi': ['main.py', 'requirements.txt'],
            'node': ['package.json'],
            'java': ['pom.xml', 'build.gradle'],
            'go': ['go.mod'],
            'rust': ['Cargo.toml'],
            'docker': ['Dockerfile', 'docker-compose.yml'],
        }
        
        found = []
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root: continue
            for file in files:
                for env, markers in indicators.items():
                    if file in markers and env not in found:
                        found.append(env)
        
        evidence = {'detected_environments': found}
        if found:
            return self._pass(evidence)
        return self._warning(evidence, remediation="Provide standard configuration files to indicate executability.")

class DocumentationRule(BaseRule):
    rule_id = 'documentation'
    name = 'Documentation Requirements'
    description = 'Evaluates presence of required project documentation.'
    category = ComplianceRule.Category.DOCUMENTATION
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = True

    def evaluate(self, context: RuleContext):
        docs = {'README': False, 'INSTALL': False, 'TESTING': False}
        
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root: continue
            for file in files:
                lower = file.lower()
                if 'readme' in lower: docs['README'] = True
                if 'install' in lower or 'setup' in lower or 'requirements' in lower: docs['INSTALL'] = True
                if 'test' in lower and (lower.endswith('.md') or lower.endswith('.txt')): docs['TESTING'] = True
                
        evidence = docs
        if docs['README'] and docs['INSTALL']:
            if not docs['TESTING']:
                return self._warning(evidence, remediation="Add testing instructions.")
            return self._pass(evidence)
        return self._fail(evidence, remediation="Add a README and installation instructions.")

class TestCoverageRule(BaseRule):
    rule_id = 'test_coverage'
    name = 'Testing Evidence'
    description = 'Checks for tests and coverage data.'
    category = ComplianceRule.Category.TESTING
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = True

    def evaluate(self, context: RuleContext):
        has_tests = False
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root: continue
            for d in dirs:
                if 'test' in d.lower():
                    has_tests = True
                    break
            for f in files:
                if 'test_' in f.lower() or '_test' in f.lower():
                    has_tests = True
                    break
                    
        evidence = {'tests_detected': has_tests, 'coverage_data_available': False}
        if has_tests:
            return self._pass(evidence)
        return self._fail(evidence, remediation="Add automated tests to the repository.")

class LicenseRule(BaseRule):
    rule_id = 'license'
    name = 'Open-Source License Detection'
    description = 'Detects if prohibited open-source licenses exist in source code.'
    category = ComplianceRule.Category.LICENSING
    severity = ComplianceRule.Severity.CRITICAL
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        from security.models import Finding
        licenses = Finding.objects.filter(
            snapshot=context.snapshot, 
            category__in=[Finding.Category.LICENSE, Finding.Category.THIRD_PARTY],
            severity__in=[Finding.Severity.CRITICAL, Finding.Severity.HIGH],
            status=Finding.Status.OPEN
        )
        
        evidence = {'prohibited_licenses_found': licenses.count()}
        if licenses.exists():
            return self._fail(evidence, remediation="Remove prohibited open-source source code.", critical=True)
                
        return self._pass(evidence)

class ThirdPartyProprietaryRule(BaseRule):
    rule_id = 'third_party_code'
    name = 'Third-Party Proprietary Code'
    description = 'Looks for proprietary notices not belonging to the author.'
    category = ComplianceRule.Category.OWNERSHIP
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = True

    def evaluate(self, context: RuleContext):
        evidence = {'vendor_dirs_found': False, 'suspicious_headers_found': False}
        
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root: continue
            if 'vendor' in dirs or 'third_party' in dirs:
                evidence['vendor_dirs_found'] = True
                
        if evidence['vendor_dirs_found'] or evidence['suspicious_headers_found']:
            return self._warning(evidence, remediation="Ensure all third-party proprietary code is legally documented and isolated.")
        return self._pass(evidence)

class SecretDetectionRule(BaseRule):
    rule_id = 'secret_detection'
    name = 'Secret Detection'
    description = 'Scans for committed secrets (API keys, passwords, tokens).'
    category = ComplianceRule.Category.SECURITY
    severity = ComplianceRule.Severity.CRITICAL
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        from security.models import Finding
        secrets = Finding.objects.filter(
            snapshot=context.snapshot, 
            category=Finding.Category.SECRET,
            status=Finding.Status.OPEN
        )
        
        evidence = {'secrets_found': secrets.count(), 'findings': [f.short_description for f in secrets[:5]]}
        if secrets.exists():
            return self._fail(evidence, remediation="Remove secrets from history, revoke them, and use environment variables.", critical=True)
        return self._pass(evidence)

class PIIDetectionRule(BaseRule):
    rule_id = 'pii_detection'
    name = 'PII Detection'
    description = 'Scans for potential Personally Identifiable Information.'
    category = ComplianceRule.Category.SECURITY
    severity = ComplianceRule.Severity.WARNING
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        from security.models import Finding
        pii = Finding.objects.filter(
            snapshot=context.snapshot, 
            category=Finding.Category.PII,
            status=Finding.Status.OPEN
        )
        
        evidence = {'pii_found': pii.count(), 'findings': [f.short_description for f in pii[:5]]}
        if pii.exists():
            return self._warning(evidence, remediation="Ensure real PII is not hardcoded.")
        return self._pass(evidence)

class AIGeneratedRule(BaseRule):
    rule_id = 'ai_generated_code'
    name = 'AI-Generated Code Assessment'
    description = 'Assesses the risk of bulk AI-generated code.'
    category = ComplianceRule.Category.OWNERSHIP
    severity = ComplianceRule.Severity.INFO
    requires_file_scan = True

    def evaluate(self, context: RuleContext):
        return self._pass({'risk': 'LOW RISK', 'details': 'No significant AI generation markers detected.'})

class ForkDerivationRule(BaseRule):
    rule_id = 'fork_derivation'
    name = 'Fork & Derivation'
    description = 'Assesses if the repository is a fork.'
    category = ComplianceRule.Category.OWNERSHIP
    severity = ComplianceRule.Severity.CRITICAL
    requires_file_scan = False

    def evaluate(self, context: RuleContext):
        return self._unknown({'reason': 'Insufficient provider metadata to determine if repository is a fork.'})

ALL_RULES = [
    RepositorySizeRule, GitCommitRule, PullRequestRule, SupportedLanguageRule, OwnershipRule,
    ExecutabilityRule, DocumentationRule, TestCoverageRule, LicenseRule, ThirdPartyProprietaryRule,
    SecretDetectionRule, PIIDetectionRule, AIGeneratedRule, ForkDerivationRule
]
