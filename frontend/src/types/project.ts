export type ProjectState = 'draft' | 'submitted' | 'under_review' | 'approved' | 'rejected' | 'archived';

export interface Project {
  id: string;
  name: string;
  short_description: string;
  state: ProjectState;
  primary_language: string;
  created_at: string;
  updated_at: string;
}

export interface DashboardData {
  projects: { total: number; active: number; draft: number; approved: number; rejected: number; };
  repositories: { connected: number; pending: number; completed: number; failed: number; };
  compliance: { passing: number; failed: number; };
  security: { critical: number; high: number; open: number; };
  recent_activity: Array<{ action: string; resource: string; timestamp: string; }>;
}
