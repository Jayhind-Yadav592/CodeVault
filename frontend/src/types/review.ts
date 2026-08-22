export interface ReviewCase {
  id: string;
  project: string; // Will hold UUID or project name
  snapshot: string;
  state: 'draft' | 'submitted' | 'triage' | 'technical_review' | 'ip_review' | 'security_review' | 'compliance_review' | 'final_review' | 'approved' | 'rejected' | 'remediation_required';
  priority: 'low' | 'normal' | 'high' | 'urgent';
  due_date: string | null;
  created_at: string;
  updated_at: string;
}

export interface ReviewComment {
  id: string;
  author_email: string;
  text: string;
  created_at: string;
}
