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
