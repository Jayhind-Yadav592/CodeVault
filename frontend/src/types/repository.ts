export interface RepositoryConnection {
  id: string;
  project: string;
  provider: string;
  repo_url: string;
  repo_name: string;
  default_branch: string;
  status: 'pending' | 'syncing' | 'synced' | 'failed';
  last_sync_time: string | null;
  last_error: string | null;
}

export interface AnalysisSnapshot {
  id: string;
  commit_hash: string;
  branch: string;
  total_files: number;
  total_loc: number;
  meaningful_loc: number;
  total_commits: number;
  meaningful_commits: number;
  languages: Array<{ language_name: string; loc: number; file_count: number }>;
  created_at: string;
}

export interface TrainPlexReadiness {
  size: { value: number; required: number; status: 'PASS' | 'FAIL' | 'UNKNOWN'; source: string };
  commits: { value: number; required: number; status: 'PASS' | 'FAIL' };
  pull_requests: { value: number; required: number; status: 'PASS' | 'FAIL' };
  quality: { tests: string; readme: string };
  ownership: { declaration: string; employer_ip: string; opensource_contamination: string };
  security: { secrets: string; pii: string };
}
