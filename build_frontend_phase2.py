import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

BASE = r"c:\Users\admin\Documents\TrainPlex\CodeVault\frontend\src"

FILES = {
    # Project Types
    "types/project.ts": """
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
""",

    # Project Service
    "services/projectService.ts": """
import api from './api';
import { Project, DashboardData } from '../types/project';

export const projectService = {
  getDashboardStats: async (): Promise<DashboardData> => {
    const response = await api.get('/projects/dashboard/');
    return response.data;
  },
  getProjects: async (params?: any): Promise<{ results: Project[], count: number }> => {
    const response = await api.get('/projects/', { params });
    return response.data;
  },
  getProject: async (id: string): Promise<Project> => {
    const response = await api.get(`/projects/${id}/`);
    return response.data;
  },
  createProject: async (data: any): Promise<Project> => {
    const response = await api.post('/projects/', data);
    return response.data;
  }
};
""",

    # Update Dashboard
    "pages/Dashboard.tsx": """
import React, { useEffect, useState } from 'react';
import { projectService } from '../services/projectService';
import { DashboardData } from '../types/project';
import { Card, CardContent, CardHeader } from '../components/ui/Card';
import { LoadingState } from '../components/ui/LoadingState';

export const Dashboard: React.FC = () => {
  const [data, setData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const stats = await projectService.getDashboardStats();
        setData(stats);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <LoadingState />;
  if (!data) return <div>Error loading dashboard</div>;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card>
          <CardHeader>Projects</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">{data.projects.total}</div>
            <div className="text-sm text-gray-500">Active: {data.projects.active} | Approved: {data.projects.approved}</div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>Repositories</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">{data.repositories.connected}</div>
            <div className="text-sm text-gray-500">Pending: {data.repositories.pending}</div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>Security Findings</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-red-600">{data.security.open}</div>
            <div className="text-sm text-gray-500">Critical: {data.security.critical} | High: {data.security.high}</div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>Compliance</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-green-600">{data.compliance.passing}</div>
            <div className="text-sm text-gray-500">Failed: {data.compliance.failed}</div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>Recent Activity</CardHeader>
        <CardContent>
          <ul className="space-y-2">
            {data.recent_activity.map((act, i) => (
              <li key={i} className="text-sm pb-2 border-b last:border-0">
                <span className="font-medium capitalize">{act.action}</span> on {act.resource} 
                <span className="text-gray-400 ml-2">{new Date(act.timestamp).toLocaleString()}</span>
              </li>
            ))}
            {data.recent_activity.length === 0 && <li className="text-gray-500">No recent activity.</li>}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
};
""",

    # Project List
    "pages/ProjectList.tsx": """
import React, { useEffect, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { projectService } from '../services/projectService';
import { Project } from '../types/project';
import { Button } from '../components/ui/Button';
import { LoadingState } from '../components/ui/LoadingState';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Badge } from '../components/ui/Badge';
import { Input } from '../components/ui/Input';

export const ProjectList: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [projects, setProjects] = useState<Project[]>([]);
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(true);
  
  const search = searchParams.get('search') || '';

  const fetchProjects = async () => {
    setLoading(true);
    try {
      const data = await projectService.getProjects({ search });
      setProjects(data.results || data); // depending on DRF pagination format
      setCount(data.count || (Array.isArray(data) ? data.length : 0));
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProjects();
  }, [search]);

  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearchParams(prev => {
      if (e.target.value) prev.set('search', e.target.value);
      else prev.delete('search');
      return prev;
    });
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Projects ({count})</h1>
        <Link to="/projects/new">
          <Button>Create Project</Button>
        </Link>
      </div>
      
      <div className="w-1/3">
        <Input placeholder="Search projects..." value={search} onChange={handleSearch} />
      </div>

      {loading ? (
        <LoadingState />
      ) : (
        <div className="bg-white rounded-lg shadow overflow-hidden">
          <Table>
            <TableHeader>
              <TableRow>
                <TableCell isHeader>Name</TableCell>
                <TableCell isHeader>Language</TableCell>
                <TableCell isHeader>Status</TableCell>
                <TableCell isHeader>Actions</TableCell>
              </TableRow>
            </TableHeader>
            <tbody>
              {projects.map(p => (
                <TableRow key={p.id}>
                  <TableCell>
                    <div className="font-medium text-gray-900">{p.name}</div>
                    <div className="text-sm text-gray-500">{p.short_description}</div>
                  </TableCell>
                  <TableCell>{p.primary_language}</TableCell>
                  <TableCell>
                    <Badge variant={p.state === 'approved' ? 'success' : 'default'}>{p.state}</Badge>
                  </TableCell>
                  <TableCell>
                    <Link to={`/projects/${p.id}`} className="text-blue-600 hover:underline">View</Link>
                  </TableCell>
                </TableRow>
              ))}
              {projects.length === 0 && (
                <TableRow>
                  <TableCell colSpan={4}>
                    <div className="text-center py-8 text-gray-500">No projects found.</div>
                  </TableCell>
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

    # Project Detail
    "pages/ProjectDetail.tsx": """
import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { projectService } from '../services/projectService';
import { Project } from '../types/project';
import { LoadingState } from '../components/ui/LoadingState';
import { Badge } from '../components/ui/Badge';
import { Card, CardContent, CardHeader } from '../components/ui/Card';

export const ProjectDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [project, setProject] = useState<Project | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (id) {
      projectService.getProject(id)
        .then(setProject)
        .catch(console.error)
        .finally(() => setLoading(false));
    }
  }, [id]);

  if (loading) return <LoadingState />;
  if (!project) return <div>Project not found</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center border-b pb-4">
        <div>
          <h1 className="text-3xl font-bold mb-2">{project.name}</h1>
          <div className="flex gap-2">
            <Badge>{project.state}</Badge>
            <Badge variant="default">{project.primary_language}</Badge>
          </div>
        </div>
      </div>
      
      <div className="flex gap-4 border-b">
        <div className="px-4 py-2 border-b-2 border-blue-600 text-blue-600 font-medium">Overview</div>
        <div className="px-4 py-2 text-gray-500 cursor-not-allowed">Repository</div>
        <div className="px-4 py-2 text-gray-500 cursor-not-allowed">Team</div>
        <div className="px-4 py-2 text-gray-500 cursor-not-allowed">Settings</div>
      </div>

      <div className="grid grid-cols-3 gap-6 mt-6">
        <div className="col-span-2 space-y-6">
          <Card>
            <CardHeader>Description</CardHeader>
            <CardContent>
              <p className="text-gray-700">{project.short_description || 'No description provided.'}</p>
            </CardContent>
          </Card>
        </div>
        <div className="col-span-1 space-y-6">
          <Card>
            <CardHeader>Details</CardHeader>
            <CardContent className="space-y-2">
              <div className="flex justify-between">
                <span className="text-gray-500">Created:</span>
                <span>{new Date(project.created_at).toLocaleDateString()}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Updated:</span>
                <span>{new Date(project.updated_at).toLocaleDateString()}</span>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};
""",

    # Project Create
    "pages/ProjectCreate.tsx": """
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { projectService } from '../services/projectService';
import { Input } from '../components/ui/Input';
import { Button } from '../components/ui/Button';

export const ProjectCreate: React.FC = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const data = {
        name,
        short_description: description,
        primary_language: 'Python', // Default for now
        development_status: 'prototype',
        project_type: 'web_application'
      };
      const proj = await projectService.createProject(data);
      navigate(`/projects/${proj.id}`);
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to create project');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto bg-white p-8 rounded-lg shadow-sm">
      <h1 className="text-2xl font-bold mb-6">Create New Project</h1>
      
      {error && <div className="p-3 mb-4 bg-red-100 text-red-700 rounded">{error}</div>}
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <Input 
          label="Project Name" 
          value={name} 
          onChange={(e) => setName(e.target.value)} 
          required 
        />
        <div className="w-full">
          <label className="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea 
            className="w-full rounded-md border border-gray-300 px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows={4}
          />
        </div>
        <div className="pt-4 flex gap-4">
          <Button type="button" variant="secondary" onClick={() => navigate('/projects')}>Cancel</Button>
          <Button type="submit" isLoading={loading}>Create Project</Button>
        </div>
      </form>
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
            <Route path="/admin" element={<div>Admin (WIP)</div>} />
          </Route>

          <Route path="/" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
"""
}

for rel_path, content in FILES.items():
    write_file(os.path.join(BASE, rel_path), content)

print("Phase 2 components and pages generated successfully!")
