import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
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
