from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import WorkflowExecution, WorkflowStepExecution, ApprovalGate
from .engines.condition_engine import ConditionEngine
from .engines.action_engine import ActionEngine

class LoopProtectionService:
    MAX_EXECUTION_DEPTH = 5
    
    @staticmethod
    def check_loop(correlation_id: str):
        if not correlation_id:
            return
            
        count = WorkflowExecution.objects.filter(correlation_id=correlation_id).count()
        if count >= LoopProtectionService.MAX_EXECUTION_DEPTH:
            raise ValidationError(f"CIRCUIT_BREAKER_TRIPPED: Workflow execution depth exceeded for correlation {correlation_id}")

class WorkflowOrchestratorService:
    @staticmethod
    def trigger_workflow(workflow_version, event_payload: dict, event_id: str, correlation_id: str):
        LoopProtectionService.check_loop(correlation_id)
        
        # Idempotency Check
        if WorkflowExecution.objects.filter(workflow_version=workflow_version, trigger_event_id=event_id).exists():
            return None # Already processed
            
        execution = WorkflowExecution.objects.create(
            workflow_version=workflow_version,
            trigger_event_id=event_id,
            correlation_id=correlation_id,
            status=WorkflowExecution.Status.RUNNING,
            started_at=timezone.now()
        )
        
        definition = workflow_version.definition_payload
        conditions = definition.get('conditions', {})
        
        # Evaluate Conditions
        if ConditionEngine.evaluate(conditions, event_payload):
            actions = definition.get('actions', [])
            for action_def in actions:
                WorkflowOrchestratorService._execute_action(execution, action_def, event_payload)
                if execution.status == WorkflowExecution.Status.WAITING_APPROVAL:
                    break # Stop executing further actions until approved
                    
            if execution.status == WorkflowExecution.Status.RUNNING:
                execution.status = WorkflowExecution.Status.COMPLETED
                execution.completed_at = timezone.now()
                execution.save()
        else:
            # Condition didn't match
            execution.status = WorkflowExecution.Status.COMPLETED
            execution.completed_at = timezone.now()
            execution.save()
            
        return execution
        
    @staticmethod
    def _execute_action(execution: WorkflowExecution, action_def: dict, context: dict):
        action_type = action_def.get('type')
        try:
            result = ActionEngine.execute_action(action_def, context)
            
            WorkflowStepExecution.objects.create(
                execution=execution,
                step_name=action_type,
                action_type=action_type,
                payload_snapshot=action_def,
                status="SUCCESS"
            )
            
            if result.get("status") == "WAITING_APPROVAL":
                execution.status = WorkflowExecution.Status.WAITING_APPROVAL
                execution.save()
                ApprovalGate.objects.create(
                    execution=execution,
                    required_role=result.get("required_role", "")
                )
                
        except Exception as e:
            WorkflowStepExecution.objects.create(
                execution=execution,
                step_name=action_type,
                action_type=action_type,
                payload_snapshot=action_def,
                status="FAILED"
            )
            execution.status = WorkflowExecution.Status.FAILED
            execution.error_message = str(e)
            execution.save()

class SimulationService:
    @staticmethod
    def simulate(workflow_version, event_payload: dict):
        definition = workflow_version.definition_payload
        conditions = definition.get('conditions', {})
        
        result = {
            "condition_matched": ConditionEngine.evaluate(conditions, event_payload),
            "expected_actions": definition.get('actions', []),
            "side_effects": "NONE (Simulation Mode)"
        }
        return result
