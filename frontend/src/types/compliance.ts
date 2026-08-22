export interface ComplianceDashboard {
  total: number;
  passing: number;
  failed: number;
  partial: number;
  unknown: number;
  manual_review: number;
  recent: Array<{ id: string; decision: string; project: string; date: string }>;
}

export interface ComplianceRule {
  id: string;
  rule_id: string;
  name: string;
  category: string;
  severity: string;
  description: string;
}

export interface ComplianceEvaluation {
  id: string;
  decision: string;
  created_at: string;
  overall_score: number;
  rules: Array<{
    rule_id: string;
    name: string;
    category: string;
    severity: string;
    status: string;
    evidence: any;
    is_critical_failure: boolean;
  }>;
}
