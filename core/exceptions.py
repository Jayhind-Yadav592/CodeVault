from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.core.exceptions import ValidationError as DjangoValidationError
import logging

logger = logging.getLogger('core')

def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django REST Framework.
    Standardizes error responses and logs errors.
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Handle Django's ValidationError (often thrown by models)
    if isinstance(exc, DjangoValidationError):
        if hasattr(exc, 'message_dict'):
            return Response({"error": "Validation Error", "details": exc.message_dict}, status=400)
        return Response({"error": "Validation Error", "details": exc.messages}, status=400)

    if response is not None:
        # Standardize standard DRF errors
        custom_response_data = {
            'error': 'API Error',
            'details': response.data
        }
        
        # Override specific status codes if needed
        if response.status_code == 404:
            custom_response_data['error'] = 'Not Found'
        elif response.status_code == 403:
            custom_response_data['error'] = 'Permission Denied'
            
        response.data = custom_response_data
    else:
        # If response is None, it means DRF couldn't handle the exception (e.g., 500 Server Error)
        logger.error(f"Unhandled Exception: {exc}", exc_info=True)
        # In a real production environment, you might want to obscure the error details unless debugging
        return Response(
            {"error": "Internal Server Error", "details": "An unexpected error occurred."},
            status=500
        )

    return response
