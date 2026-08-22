import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { ProjectList } from './ProjectList';
import { projectService } from '../services/projectService';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/projectService');

describe('ProjectList', () => {
  it('renders correctly with empty data', async () => {
    vi.mocked(projectService.getProjects).mockResolvedValue({ results: [], count: 0 });

    render(<BrowserRouter><ProjectList /></BrowserRouter>);
    
    await waitFor(() => {
      expect(screen.getByText('Projects (0)')).toBeInTheDocument();
    });
    
    expect(screen.getByText('No projects found.')).toBeInTheDocument();
  });

  it('renders project rows', async () => {
    vi.mocked(projectService.getProjects).mockResolvedValue({ 
      results: [
        { id: '1', name: 'Test Proj', short_description: 'Desc', primary_language: 'Python', state: 'approved', created_at: '', updated_at: '' }
      ], 
      count: 1 
    });

    render(<BrowserRouter><ProjectList /></BrowserRouter>);
    
    await waitFor(() => {
      expect(screen.getByText('Test Proj')).toBeInTheDocument();
    });
  });
});
