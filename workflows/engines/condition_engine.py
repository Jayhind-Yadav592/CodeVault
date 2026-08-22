import json

class ConditionEngine:
    """
    Safely parses JSON-based Abstract Syntax Trees (ASTs) to evaluate conditions
    against a deterministic payload context. Prevents arbitrary Python evaluation.
    """
    
    ALLOWED_OPERATORS = {
        'equals': lambda x, y: x == y,
        'not_equals': lambda x, y: x != y,
        'greater_than': lambda x, y: x > y if isinstance(x, (int, float)) and isinstance(y, (int, float)) else False,
        'less_than': lambda x, y: x < y if isinstance(x, (int, float)) and isinstance(y, (int, float)) else False,
        'contains': lambda x, y: y in x if isinstance(x, (str, list)) else False,
    }
    
    @staticmethod
    def evaluate(ast: dict, context: dict) -> bool:
        if not ast:
            return True
            
        logical_op = ast.get('operator', 'AND').upper()
        rules = ast.get('rules', [])
        
        if not rules:
            return True
            
        results = []
        for rule in rules:
            if 'operator' in rule and 'rules' in rule: # Nested group
                results.append(ConditionEngine.evaluate(rule, context))
            else: # Leaf rule
                field = rule.get('field')
                op = rule.get('condition')
                target = rule.get('value')
                
                # We do NOT allow eval() here. We extract safely from context.
                # Example: field = "security.critical_findings"
                actual_val = ConditionEngine._get_nested_value(context, field)
                
                if op in ConditionEngine.ALLOWED_OPERATORS:
                    results.append(ConditionEngine.ALLOWED_OPERATORS[op](actual_val, target))
                else:
                    results.append(False) # Unknown operator fails safe
                    
        if logical_op == 'AND':
            return all(results)
        elif logical_op == 'OR':
            return any(results)
        elif logical_op == 'NOT':
            return not all(results)
            
        return False
        
    @staticmethod
    def _get_nested_value(context: dict, path: str):
        parts = path.split('.')
        current = context
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
            else:
                return None
        return current

    @staticmethod
    def validate_ast(ast: dict):
        """Validates that the AST contains NO dangerous constructs."""
        # By strict schema definition, we enforce JSON limits, avoiding eval completely.
        # Stringifying and checking for python builtins is a primitive fallback.
        serialized = json.dumps(ast)
        dangerous_tokens = ['__import__', 'eval', 'exec', 'subprocess', 'os.', 'sys.']
        for token in dangerous_tokens:
            if token in serialized:
                raise ValueError(f"Dangerous token detected in AST: {token}")
