from django.core.exceptions import ValidationError

class ActionEngine:
    """
    Controlled registry of whitelisted actions to execute securely.
    """
    
    @staticmethod
    def execute_action(action_def: dict, execution_context: dict):
        action_type = action_def.get('type')
        params = action_def.get('params', {})
        
        # We explicitly map string types to safe functions
        action_map = {
            'CREATE_TASK': ActionEngine._create_task,
            'SEND_NOTIFICATION': ActionEngine._send_notification,
            'PAUSE_PROJECT': ActionEngine._pause_project,
            'REQUEST_APPROVAL': ActionEngine._request_approval,
        }
        
        if action_type not in action_map:
            raise ValidationError(f"Unauthorized or unknown action type: {action_type}")
            
        # Execute safely mapped method
        return action_map[action_type](params, execution_context)
        
    @staticmethod
    def _create_task(params: dict, context: dict):
        # Mocks integrating with Phase 13 ProjectTask
        return {"status": "SUCCESS", "detail": f"Task '{params.get('title')}' created."}
        
    @staticmethod
    def _send_notification(params: dict, context: dict):
        # Mocks integrating with Phase 5 Notifications
        return {"status": "SUCCESS", "detail": "Notification dispatched."}
        
    @staticmethod
    def _pause_project(params: dict, context: dict):
        return {"status": "SUCCESS", "detail": "Project paused."}
        
    @staticmethod
    def _request_approval(params: dict, context: dict):
        # The Orchestrator will intercept this and generate an ApprovalGate
        return {"status": "WAITING_APPROVAL", "required_role": params.get('role')}
