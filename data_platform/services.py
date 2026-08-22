import json
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import (
    EventSchema, DomainEvent, ConsumerCheckpoint,
    EventProcessingError, DimDate, DimProject,
    FactRepositoryAnalysis, FactLicense
)

class EventDispatcherService:
    @staticmethod
    def dispatch(event_type: str, aggregate_type: str, aggregate_id: str, payload: dict, actor=None, version='v1') -> DomainEvent:
        schema = EventSchema.objects.filter(event_type=event_type, version=version, status=EventSchema.Status.ACTIVE).first()
        if schema:
            for req in schema.required_fields:
                if req not in payload:
                    raise ValidationError(f"Missing required field {req} in payload for {event_type}:{version}")
                    
        return DomainEvent.objects.create(
            event_type=event_type,
            event_version=version,
            aggregate_type=aggregate_type,
            aggregate_id=str(aggregate_id),
            payload=payload,
            actor=actor
        )

class EventConsumerBase:
    consumer_name = "BaseConsumer"
    
    def process(self, event: DomainEvent):
        raise NotImplementedError()
        
    def execute(self, event: DomainEvent):
        try:
            with transaction.atomic():
                self.process(event)
                # Update checkpoint
                cp, _ = ConsumerCheckpoint.objects.get_or_create(consumer_name=self.consumer_name, defaults={
                    'last_processed_timestamp': event.timestamp,
                    'last_processed_event_id': str(event.id)
                })
                cp.last_processed_timestamp = event.timestamp
                cp.last_processed_event_id = str(event.id)
                cp.save()
        except Exception as e:
            EventProcessingError.objects.create(
                event=event,
                consumer_name=self.consumer_name,
                error_message=str(e),
                status=EventProcessingError.Status.DEAD_LETTER
            )
            # In a real system, we'd log and trigger alerts

class AnalyticsProjectionService(EventConsumerBase):
    consumer_name = "AnalyticsWarehouseConsumer"
    
    def process(self, event: DomainEvent):
        date_obj = event.timestamp.date()
        dim_date, _ = DimDate.objects.get_or_create(date=date_obj, defaults={
            'year': date_obj.year, 'month': date_obj.month,
            'day': date_obj.day, 'quarter': (date_obj.month - 1) // 3 + 1
        })
        
        if event.event_type == 'project.created':
            DimProject.objects.create(
                original_project_id=event.aggregate_id,
                name=event.payload.get('name', 'Unknown'),
                category=event.payload.get('category', 'Unknown'),
                primary_language=event.payload.get('language', 'Unknown')
            )
            
        elif event.event_type == 'repository.analysis.completed':
            dim_proj = DimProject.objects.filter(original_project_id=event.aggregate_id).order_by('-valid_from').first()
            if dim_proj:
                # Idempotency check
                if FactRepositoryAnalysis.objects.filter(event_reference=event).exists():
                    return # Already processed
                
                FactRepositoryAnalysis.objects.create(
                    date=dim_date,
                    project=dim_proj,
                    analysis_duration_seconds=event.payload.get('duration', 0),
                    approximate_loc=event.payload.get('loc', 0),
                    is_successful=event.payload.get('success', True),
                    event_reference=event
                )
        
        elif event.event_type == 'license.activated':
            dim_proj = DimProject.objects.filter(original_project_id=event.payload.get('project_id')).order_by('-valid_from').first()
            if dim_proj:
                if FactLicense.objects.filter(event_reference=event).exists():
                    return
                
                # Replay protection: we must be absolutely careful not to double count
                FactLicense.objects.create(
                    date=dim_date,
                    project=dim_proj,
                    license_type=event.payload.get('type', 'Unknown'),
                    revenue_amount=event.payload.get('amount', 0),
                    event_reference=event
                )

class QueryParserService:
    @staticmethod
    def parse_advanced_query(query_string: str) -> dict:
        """Parses 'language:python category:fintech' into a dict"""
        filters = {}
        parts = query_string.split()
        for part in parts:
            if ':' in part:
                k, v = part.split(':', 1)
                filters[k] = v
        return filters
