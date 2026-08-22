import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

BASE = r"c:\Users\admin\Documents\TrainPlex\CodeVault\frontend\src"

FILES = {
    # Types
    "types/repository.ts": """
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
""",

    # Service
    "services/repositoryService.ts": """
import api from './api';
import { RepositoryConnection, AnalysisSnapshot, TrainPlexReadiness } from '../types/repository';

export const repositoryService = {
  getConnections: async (): Promise<{ results: RepositoryConnection[] }> => {
    const response = await api.get('/repositories/connections/');
    return response.data;
  },
  getConnection: async (id: string): Promise<RepositoryConnection> => {
    const response = await api.get(`/repositories/connections/${id}/`);
    return response.data;
  },
  connectRepository: async (data: any): Promise<RepositoryConnection> => {
    const response = await api.post('/repositories/connections/', data);
    return response.data;
  },
  syncRepository: async (id: string): Promise<any> => {
    const response = await api.post(`/repositories/connections/${id}/sync/`);
    return response.data;
  },
  getLatestSnapshot: async (id: string): Promise<AnalysisSnapshot> => {
    const response = await api.get(`/repositories/connections/${id}/latest_snapshot/`);
    return response.data;
  },
  getTrainPlexReadiness: async (id: string): Promise<TrainPlexReadiness> => {
    const response = await api.get(`/repositories/connections/${id}/trainplex_readiness/`);
    return response.data;
  }
};
""",

    # Connect Page
    "pages/RepositoryConnect.tsx": """
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { repositoryService } from '../services/repositoryService';
import { projectService } from '../services/projectService';
import { Input } from '../components/ui/Input';
import { Button } from '../components/ui/Button';
import { Project } from '../types/project';

export const RepositoryConnect: React.FC = () => {
  const [url, setUrl] = useState('');
  const [provider, setProvider] = useState('github');
  const [projectId, setProjectId] = useState('');
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    projectService.getProjects().then(data => setProjects(data.results || data as any));
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const conn = await repositoryService.connectRepository({
        project: projectId,
        provider,
        repo_url: url,
        default_branch: 'main'
      });
      navigate(`/repositories/${conn.id}`);
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to connect repository');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto bg-white p-8 rounded shadow-sm">
      <h1 className="text-2xl font-bold mb-6">Connect Repository</h1>
      {error && <div className="text-red-600 bg-red-50 p-3 mb-4 rounded">{error}</div>}
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-1">Project</label>
          <select 
            className="w-full border p-2 rounded focus:ring-2 focus:ring-blue-500" 
            value={projectId} 
            onChange={e => setProjectId(e.target.value)}
            required
          >
            <option value="">Select a project...</option>
            {projects.map(p => <option key={p.id} value={p.id}>{p.name}</option>)}
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Provider</label>
          <select 
            className="w-full border p-2 rounded focus:ring-2 focus:ring-blue-500" 
            value={provider} 
            onChange={e => setProvider(e.target.value)}
          >
            <option value="github">GitHub</option>
            <option value="gitlab">GitLab</option>
            <option value="bitbucket">Bitbucket</option>
          </select>
        </div>
        <Input label="Repository URL" value={url} onChange={e => setUrl(e.target.value)} placeholder="https://github.com/org/repo" required />
        <div className="pt-4">
          <Button type="submit" isLoading={loading}>Connect Repository</Button>
        </div>
      </form>
    </div>
  );
};
""",

    # Repository List
    "pages/RepositoryList.tsx": """
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { repositoryService } from '../services/repositoryService';
import { RepositoryConnection } from '../types/repository';
import { Button } from '../components/ui/Button';
import { LoadingState } from '../components/ui/LoadingState';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Badge } from '../components/ui/Badge';

export const RepositoryList: React.FC = () => {
  const [repos, setRepos] = useState<RepositoryConnection[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    repositoryService.getConnections().then(data => {
      setRepos(data.results || data as any);
    }).finally(() => setLoading(false));
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Repositories</h1>
        <Link to="/repositories/connect">
          <Button>Connect Repository</Button>
        </Link>
      </div>

      {loading ? <LoadingState /> : (
        <div className="bg-white shadow rounded">
          <Table>
            <TableHeader>
              <TableRow>
                <TableCell isHeader>Repository</TableCell>
                <TableCell isHeader>Provider</TableCell>
                <TableCell isHeader>Status</TableCell>
                <TableCell isHeader>Actions</TableCell>
              </TableRow>
            </TableHeader>
            <tbody>
              {repos.map(r => (
                <TableRow key={r.id}>
                  <TableCell>
                    <div className="font-medium">{r.repo_url}</div>
                    <div className="text-sm text-gray-500">{r.default_branch}</div>
                  </TableCell>
                  <TableCell className="capitalize">{r.provider}</TableCell>
                  <TableCell>
                    <Badge variant={r.status === 'synced' ? 'success' : r.status === 'failed' ? 'danger' : 'warning'}>
                      {r.status}
                    </Badge>
                  </TableCell>
                  <TableCell>
                    <Link to={`/repositories/${r.id}`} className="text-blue-600 hover:underline">Manage</Link>
                  </TableCell>
                </TableRow>
              ))}
              {repos.length === 0 && (
                <TableRow>
                  <TableCell colSpan={4}><div className="py-6 text-center text-gray-500">No repositories connected.</div></TableCell>
                </TableRow>
              )}
            </tbody>
          </Table>
        </div>
      )}
    </div>
  );
};
""",

    # Repository Detail
    "pages/RepositoryDetail.tsx": """
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { repositoryService } from '../services/repositoryService';
import { RepositoryConnection, AnalysisSnapshot, TrainPlexReadiness } from '../types/repository';
import { LoadingState } from '../components/ui/LoadingState';
import { Badge } from '../components/ui/Badge';
import { Card, CardHeader, CardContent } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Alert } from '../components/ui/Alert';

export const RepositoryDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [repo, setRepo] = useState<RepositoryConnection | null>(null);
  const [snapshot, setSnapshot] = useState<AnalysisSnapshot | null>(null);
  const [readiness, setReadiness] = useState<TrainPlexReadiness | null>(null);
  const [loading, setLoading] = useState(true);
  const [syncing, setSyncing] = useState(false);
  const [tab, setTab] = useState('overview');

  const fetchData = async () => {
    if (!id) return;
    try {
      const r = await repositoryService.getConnection(id);
      setRepo(r);
      if (r.status === 'synced') {
        const snap = await repositoryService.getLatestSnapshot(id).catch(() => null);
        setSnapshot(snap);
        const ready = await repositoryService.getTrainPlexReadiness(id).catch(() => null);
        setReadiness(ready);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchData(); }, [id]);

  const handleSync = async () => {
    if (!id) return;
    setSyncing(true);
    try {
      await repositoryService.syncRepository(id);
      alert('Analysis triggered! Refresh in a few minutes.');
      fetchData();
    } catch (e) {
      alert('Failed to trigger analysis');
    } finally {
      setSyncing(false);
    }
  };

  if (loading) return <LoadingState />;
  if (!repo) return <div>Repository not found</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center border-b pb-4">
        <div>
          <h1 className="text-3xl font-bold mb-1">{repo.repo_name || repo.repo_url}</h1>
          <Badge>{repo.status}</Badge>
        </div>
        <Button onClick={handleSync} isLoading={syncing}>Analyze Repository</Button>
      </div>

      <div className="flex gap-4 border-b overflow-x-auto">
        <button onClick={() => setTab('overview')} className={`px-4 py-2 ${tab === 'overview' ? 'border-b-2 border-blue-600 font-medium text-blue-600' : 'text-gray-500'}`}>Overview & Git</button>
        <button onClick={() => setTab('readiness')} className={`px-4 py-2 ${tab === 'readiness' ? 'border-b-2 border-blue-600 font-medium text-blue-600' : 'text-gray-500'}`}>TrainPlex Readiness</button>
      </div>

      {tab === 'overview' && (
        <div className="grid grid-cols-2 gap-6">
          <Card>
            <CardHeader>Repository Information</CardHeader>
            <CardContent className="space-y-2">
              <div className="flex justify-between"><span>Provider:</span> <span className="capitalize">{repo.provider}</span></div>
              <div className="flex justify-between"><span>Branch:</span> <span>{repo.default_branch}</span></div>
              <div className="flex justify-between"><span>URL:</span> <a href={repo.repo_url} target="_blank" rel="noreferrer" className="text-blue-500 hover:underline">Link</a></div>
            </CardContent>
          </Card>
          
          {snapshot ? (
            <Card>
              <CardHeader>Git & Code Metrics</CardHeader>
              <CardContent className="space-y-2">
                <div className="flex justify-between"><span>Total LOC:</span> <span>{snapshot.total_loc?.toLocaleString() || 0}</span></div>
                <div className="flex justify-between font-medium"><span>Meaningful LOC:</span> <span>{snapshot.meaningful_loc?.toLocaleString() || 0}</span></div>
                <div className="flex justify-between"><span>Commits:</span> <span>{snapshot.meaningful_commits?.toLocaleString() || 0}</span></div>
                <div className="flex justify-between"><span>Files:</span> <span>{snapshot.total_files?.toLocaleString() || 0}</span></div>
              </CardContent>
            </Card>
          ) : (
            <Card><CardContent className="pt-6"><Alert type="warning">No analysis data available. Please analyze the repository.</Alert></CardContent></Card>
          )}
        </div>
      )}

      {tab === 'readiness' && readiness && (
        <div className="space-y-6">
          <h2 className="text-xl font-bold">TrainPlex Readiness Evaluation</h2>
          <div className="grid grid-cols-2 gap-4">
            <Card>
              <CardHeader>Volume Requirements</CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Minimum 50,000 LOC</span>
                  <div className="flex items-center gap-2">
                    <span className="text-sm text-gray-500">Actual: {readiness.size.value}</span>
                    <Badge variant={readiness.size.status === 'PASS' ? 'success' : 'danger'}>{readiness.size.status}</Badge>
                  </div>
                </div>
                <div className="flex justify-between items-center border-b pb-2">
                  <span>5+ Meaningful Commits</span>
                  <div className="flex items-center gap-2">
                    <span className="text-sm text-gray-500">Actual: {readiness.commits.value}</span>
                    <Badge variant={readiness.commits.status === 'PASS' ? 'success' : 'danger'}>{readiness.commits.status}</Badge>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>Legal & Security</CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Creator Ownership</span>
                  <Badge variant={readiness.ownership.declaration === 'PASS' ? 'success' : 'warning'}>{readiness.ownership.declaration}</Badge>
                </div>
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Open Source Contamination</span>
                  <Badge variant="warning">{readiness.ownership.opensource_contamination}</Badge>
                </div>
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Secret Exposure</span>
                  <Badge variant="success">{readiness.security.secrets}</Badge>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      )}
      {tab === 'readiness' && !readiness && (
        <Alert type="error">Readiness data requires a completed repository analysis.</Alert>
      )}
    </div>
  );
};
""",

    # Update App.tsx
    "App.tsx": """
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { PublicLayout } from './layouts/PublicLayout';
import { AuthenticatedLayout } from './layouts/AuthenticatedLayout';
import { Login } from './pages/Login';
import { Dashboard } from './pages/Dashboard';
import { ProjectList } from './pages/ProjectList';
import { ProjectDetail } from './pages/ProjectDetail';
import { ProjectCreate } from './pages/ProjectCreate';
import { RepositoryList } from './pages/RepositoryList';
import { RepositoryConnect } from './pages/RepositoryConnect';
import { RepositoryDetail } from './pages/RepositoryDetail';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route element={<PublicLayout />}>
            <Route path="/login" element={<Login />} />
          </Route>
          
          <Route element={<AuthenticatedLayout />}>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/projects" element={<ProjectList />} />
            <Route path="/projects/new" element={<ProjectCreate />} />
            <Route path="/projects/:id" element={<ProjectDetail />} />
            
            <Route path="/repositories" element={<RepositoryList />} />
            <Route path="/repositories/connect" element={<RepositoryConnect />} />
            <Route path="/repositories/:id" element={<RepositoryDetail />} />
            
            <Route path="/admin" element={<div>Admin (WIP)</div>} />
          </Route>

          <Route path="/" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
""",
    
    # Update AuthenticatedLayout Sidebar
    "layouts/AuthenticatedLayout.tsx": """
import React from 'react';
import { Outlet, Navigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export const AuthenticatedLayout: React.FC = () => {
  const { user, loading, logout } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <Navigate to="/login" replace />;

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <nav className="bg-blue-900 text-white shadow-sm px-6 py-3 flex justify-between items-center">
        <div className="font-bold text-xl tracking-wider">CODEVAULT</div>
        <div className="flex gap-4 items-center">
          <span className="text-sm opacity-80">{user.email}</span>
          <button onClick={logout} className="text-sm bg-blue-800 px-3 py-1 rounded hover:bg-blue-700 transition">Logout</button>
        </div>
      </nav>
      <div className="flex flex-1">
        <aside className="w-64 bg-white shadow-md border-r border-gray-200">
          <ul className="p-4 space-y-2">
            <li><Link to="/dashboard" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Dashboard</Link></li>
            <li><Link to="/projects" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Projects</Link></li>
            <li><Link to="/repositories" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Repositories</Link></li>
          </ul>
        </aside>
        <main className="flex-1 p-8 overflow-y-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
""",
    
    # Test file
    "pages/RepositoryList.test.tsx": """
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { RepositoryList } from './RepositoryList';
import { repositoryService } from '../services/repositoryService';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/repositoryService');

describe('RepositoryList', () => {
  it('renders correctly with empty data', async () => {
    vi.mocked(repositoryService.getConnections).mockResolvedValue({ results: [] });

    render(<BrowserRouter><RepositoryList /></BrowserRouter>);
    
    await waitFor(() => {
      expect(screen.getByText('Repositories')).toBeInTheDocument();
    });
    
    expect(screen.getByText('No repositories connected.')).toBeInTheDocument();
  });
});
"""
}

for rel_path, content in FILES.items():
    write_file(os.path.join(BASE, rel_path), content)

print("Phase 3 components and pages generated successfully!")
