import React, { useEffect, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { projectService } from '../services/projectService';
import type { Project } from '../types/project';
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

  useEffect(() => {
    const fetchProjects = async () => {
      setLoading(true);
      try {
        const data = await projectService.getProjects({ search });
        setProjects(data.results || data);
        setCount(data.count || (Array.isArray(data) ? data.length : 0));
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
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
