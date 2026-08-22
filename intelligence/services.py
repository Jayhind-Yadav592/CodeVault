from django.core.exceptions import ValidationError
from .models import (
    FeatureVector, Dataset, DatasetSplit, ModelRegistry,
    Prediction, PredictionFeedback, ModelEvaluation
)
from repositories.models import AnalysisSnapshot
from security.models import Finding
from math import sqrt
from django.db.models import Count

class FeatureExtractionService:
    @staticmethod
    def extract_features(snapshot: AnalysisSnapshot, version='v1.0') -> FeatureVector:
        # Check if exists
        existing = FeatureVector.objects.filter(snapshot=snapshot, version=version).first()
        if existing:
            return existing

        project = snapshot.repository.project
        
        # Calculate raw signals
        loc = project.approximate_loc
        language = project.primary_language
        findings = Finding.objects.filter(snapshot=snapshot)
        critical_findings = findings.filter(severity=Finding.Severity.CRITICAL).count()
        total_findings = findings.count()
        
        # We assume 1 point of maturity for every 10,000 LOC up to 10
        scale = min(loc / 10000, 10) if loc else 0
        
        features = {
            'loc': loc,
            'primary_language': language,
            'critical_security_findings': critical_findings,
            'total_security_findings': total_findings,
            'scale_factor': scale,
            # In a real scenario, we would parse test file counts, Git commit freq, etc.
            'test_ratio': 0.15, 
            'doc_ratio': 0.05
        }
        
        vector = FeatureVector.objects.create(
            snapshot=snapshot,
            version=version,
            features=features
        )
        return vector

class InferenceService:
    @staticmethod
    def predict_repository_maturity(feature_vector: FeatureVector, model: ModelRegistry) -> Prediction:
        if model.status != ModelRegistry.Status.PRODUCTION:
            raise ValidationError("Model must be in PRODUCTION for inference.")
            
        features = feature_vector.features
        loc = features.get('loc', 0)
        critical_findings = features.get('critical_security_findings', 0)
        
        # A simple simulated heuristic model representing ML logic
        score = 0
        if loc > 50000:
            score += 40
        elif loc > 10000:
            score += 20
            
        if features.get('test_ratio', 0) > 0.1:
            score += 30
            
        if critical_findings == 0:
            score += 30
        else:
            score -= (critical_findings * 10)
            
        if score >= 80:
            label = 'VERY_HIGH'
        elif score >= 60:
            label = 'HIGH'
        elif score >= 40:
            label = 'MEDIUM'
        else:
            label = 'LOW'
            
        explanation = {
            'contributing_features': {
                'loc': loc,
                'critical_findings': critical_findings,
                'test_ratio': features.get('test_ratio')
            },
            'model_type': model.model_type
        }
        
        return Prediction.objects.create(
            model=model,
            feature_vector=feature_vector,
            predicted_label=label,
            confidence=0.85, # simulated confidence
            explanation=explanation
        )

class SimilarityService:
    @staticmethod
    def find_similar(target_vector: FeatureVector, model: ModelRegistry, limit=5):
        if model.model_type != ModelRegistry.Type.SIMILARITY:
            raise ValidationError("Model must be a similarity model.")
            
        target_features = target_vector.features
        target_loc = target_features.get('loc', 0)
        
        # In a real ML engine, this would be a vector DB query or cosine similarity matrix.
        # Here we do a simulated heuristic search matching LOC scale.
        
        all_vectors = FeatureVector.objects.exclude(id=target_vector.id)
        results = []
        
        for vec in all_vectors:
            vec_loc = vec.features.get('loc', 0)
            # Simple 1D distance
            distance = abs(target_loc - vec_loc)
            similarity_score = max(100 - (distance / 1000), 0) / 100
            
            if similarity_score > 0.5:
                results.append({
                    'feature_vector_id': str(vec.id),
                    'snapshot_id': str(vec.snapshot.id),
                    'similarity': similarity_score,
                    'reasons': [f"Similar LOC footprint (distance {distance})"]
                })
                
        # Sort desc
        results.sort(key=lambda x: x['similarity'], reverse=True)
        return results[:limit]

class ReviewAssistantService:
    @staticmethod
    def generate_summary(snapshot: AnalysisSnapshot) -> str:
        # A deterministic, safe, explainable text generation based on real data
        project = snapshot.repository.project
        
        findings = Finding.objects.filter(snapshot=snapshot)
        critical = findings.filter(severity=Finding.Severity.CRITICAL).count()
        
        lines = []
        lines.append("### Reviewer Summary")
        lines.append("")
        lines.append("#### Strengths:")
        if project.approximate_loc > 10000:
            lines.append(f"- Massive codebase: {project.approximate_loc} LOC")
        
        lines.append("")
        lines.append("#### Review Attention:")
        if critical > 0:
            lines.append(f"- {critical} critical security findings require immediate review.")
        else:
            lines.append("- Zero critical security findings.")
            
        return "\n".join(lines)
