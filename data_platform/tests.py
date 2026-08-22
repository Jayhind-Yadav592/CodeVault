import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import DomainEvent, FactRepositoryAnalysis, FactLicense, EventProcessingError
from .services import EventDispatcherService, AnalyticsProjectionService

User = get_user_model()

@pytest.fixture
def data_setup(db):
    user = User.objects.create_user(email='data@test.com', password='pw')
    return user

@pytest.mark.django_db
def test_domain_event_immutability(data_setup):
    event = EventDispatcherService.dispatch(
        event_type='project.created',
        aggregate_type='Project',
        aggregate_id='proj-123',
        payload={'name': 'Test', 'category': 'FinTech', 'language': 'Python'},
        actor=data_setup
    )
    
    # Try modifying and saving
    event.payload = {'name': 'Hacked'}
    with pytest.raises(ValidationError):
        event.save()
        
    event.refresh_from_db()
    assert event.payload['name'] == 'Test'

@pytest.mark.django_db
def test_analytics_idempotency_and_projections(data_setup):
    # 1. Project created
    proj_event = EventDispatcherService.dispatch(
        event_type='project.created',
        aggregate_type='Project',
        aggregate_id='proj-456',
        payload={'name': 'AnalyticsApp', 'category': 'Data', 'language': 'Go'},
        actor=data_setup
    )
    
    consumer = AnalyticsProjectionService()
    consumer.execute(proj_event)
    
    # 2. Analysis completed
    analysis_event = EventDispatcherService.dispatch(
        event_type='repository.analysis.completed',
        aggregate_type='Project',
        aggregate_id='proj-456',
        payload={'duration': 45, 'loc': 12000, 'success': True},
        actor=data_setup
    )
    
    consumer.execute(analysis_event)
    assert FactRepositoryAnalysis.objects.count() == 1
    
    # Execute identical event again (Idempotency test)
    consumer.execute(analysis_event)
    # Count should still be 1!
    assert FactRepositoryAnalysis.objects.count() == 1

@pytest.mark.django_db
def test_dead_letter_queue_handling(data_setup):
    # Simulate a bad event that causes the consumer to throw an error
    class BadConsumer(AnalyticsProjectionService):
        def process(self, event):
            raise Exception("Simulated Processing Error")
            
    bad_consumer = BadConsumer()
    
    event = EventDispatcherService.dispatch(
        event_type='bad.event',
        aggregate_type='Test',
        aggregate_id='1',
        payload={},
        actor=data_setup
    )
    
    bad_consumer.execute(event)
    
    # Should have caught exception and written to DLQ
    dlq_entries = EventProcessingError.objects.filter(status=EventProcessingError.Status.DEAD_LETTER)
    assert dlq_entries.count() == 1
    assert "Simulated Processing Error" in dlq_entries.first().error_message
