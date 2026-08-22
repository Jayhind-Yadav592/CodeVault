import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { repositoryService } from '../services/repositoryService';
import { projectService } from '../services/projectService';
import { Input } from '../components/ui/Input';
import { Button } from '../components/ui/Button';
import type { Project } from '../types/project';

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
