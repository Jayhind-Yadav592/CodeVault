import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { projectService } from '../services/projectService';
import type { Project } from '../types/project';
import { LoadingState } from '../components/ui/LoadingState';
import { Badge } from '../components/ui/Badge';
import { Card, CardContent, CardHeader } from '../components/ui/Card';

export const ProjectDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [project, setProject] = useState<Project | null>(null);
  const [loading, setLoading] = useState(true);
  const [tab, setTab] = useState('overview');

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
        <button onClick={() => setTab('overview')} className={`px-4 py-2 font-medium ${tab === 'overview' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Overview</button>
        <button onClick={() => setTab('repository')} className={`px-4 py-2 font-medium ${tab === 'repository' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Repository</button>
        <button onClick={() => setTab('team')} className={`px-4 py-2 font-medium ${tab === 'team' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Team</button>
        <button onClick={() => setTab('settings')} className={`px-4 py-2 font-medium ${tab === 'settings' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-slate-600 hover:text-slate-900'}`}>Settings</button>
      </div>

      {tab === 'overview' && (
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
                <span className="text-gray-900">Created:</span>
                <span>{new Date(project.created_at).toLocaleDateString()}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-900">Updated:</span>
                <span>{new Date(project.updated_at).toLocaleDateString()}</span>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
      )}
      {tab !== 'overview' && (
        <div className="py-12 flex flex-col items-center justify-center bg-white rounded-[18px] border border-slate-200 mt-6 shadow-sm">
          <h3 className="text-lg font-semibold text-slate-800">No Data Available</h3>
          <p className="text-slate-500 mt-2">This section has no records or configuration yet.</p>
        </div>
      )}
    </div>
  );
};
