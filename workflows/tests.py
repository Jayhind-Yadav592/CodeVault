import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import Workflow, WorkflowVersion, WorkflowExecution
from .engines.condition_engine import ConditionEngine
from .services import WorkflowOrchestratorService, LoopProtectionService, SimulationService

User = get_user_model()

@pytest.fixture
def workflow_setup(db):
    wf = Workflow.objects.create(name="Security Alert", trigger_type="security.finding")
    definition = {
        "conditions": {
            "operator": "AND",
            "rules": [
                {"field": "severity", "condition": "equals", "value": "CRITICAL"}
            ]
        },
        "actions": [
            {"type": "CREATE_TASK", "params": {"title": "Fix Vuln"}}
        ]
    }
    wv = WorkflowVersion.objects.create(workflow=wf, definition_payload=definition, is_active=True)
    return wf, wv

@pytest.mark.django_db
def test_condition_engine_rejects_eval():
    # Attempting to use Python builtins in standard condition AST parsing
    malicious_ast = {
        "operator": "AND",
        "rules": [
            {"field": "__import__('os').system('rm -rf /')", "condition": "equals", "value": "CRITICAL"}
        ]
    }
    
    with pytest.raises(ValueError, match="Dangerous token detected in AST"):
        ConditionEngine.validate_ast(malicious_ast)

@pytest.mark.django_db
def test_workflow_version_immutability(workflow_setup):
    wf, wv = workflow_setup
    
    # Verify active workflow payload cannot be modified
    wv.definition_payload = {"hacked": True}
    with pytest.raises(ValidationError):
        wv.save()

@pytest.mark.django_db
def test_loop_protection(workflow_setup):
    wf, wv = workflow_setup
    
    # Force the correlation count to max manually
    for _ in range(5):
        WorkflowExecution.objects.create(
            workflow_version=wv, 
            trigger_event_id="dummy", 
            correlation_id="loop_corr_123"
        )
        
    with pytest.raises(ValidationError, match="CIRCUIT_BREAKER_TRIPPED"):
        LoopProtectionService.check_loop("loop_corr_123")

@pytest.mark.django_db
def test_idempotency(workflow_setup):
    wf, wv = workflow_setup
    payload = {"severity": "CRITICAL"}
    
    ex1 = WorkflowOrchestratorService.trigger_workflow(wv, payload, event_id="evt_123", correlation_id="c1")
    assert ex1 is not None
    assert ex1.status == WorkflowExecution.Status.COMPLETED
    
    # Try triggering the exact same event
    ex2 = WorkflowOrchestratorService.trigger_workflow(wv, payload, event_id="evt_123", correlation_id="c1")
    assert ex2 is None # Idempotency tripped, returns None to ignore
    
    assert WorkflowExecution.objects.count() == 1

@pytest.mark.django_db
def test_simulation(workflow_setup):
    wf, wv = workflow_setup
    payload = {"severity": "CRITICAL"}
    
    sim = SimulationService.simulate(wv, payload)
    assert sim["condition_matched"] is True
    assert sim["side_effects"] == "NONE (Simulation Mode)"
    assert WorkflowExecution.objects.count() == 0 # Simulation must not save DB records
