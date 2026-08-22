export interface Finding {
  id: string;
  category: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  confidence: 'LOW' | 'MEDIUM' | 'HIGH';
  status: 'open' | 'acknowledged' | 'resolved' | 'false_positive' | 'suppressed';
  file_path: string;
  line_number: number | null;
  rule_identifier: string;
  short_description: string;
  redacted_evidence: string;
  remediation: string;
  created_at: string;
  updated_at: string;
}

export interface SecurityScanJob {
  id: string;
  status: 'queued' | 'running' | 'completed' | 'failed' | 'cancelled';
  error_message?: string;
  created_at: string;
  completed_at?: string;
}
