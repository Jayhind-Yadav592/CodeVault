import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

BASE = r"c:\Users\admin\Documents\TrainPlex\CodeVault\frontend\src"

TEST_FILES = {
    "pages/Dashboard.test.tsx": """
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { Dashboard } from './Dashboard';
import { projectService } from '../services/projectService';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/projectService');

describe('Dashboard', () => {
  it('renders loading state initially', () => {
    vi.mocked(projectService.getDashboardStats).mockReturnValue(new Promise(() => {}));
    render(<BrowserRouter><Dashboard /></BrowserRouter>);
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });

  it('renders data correctly', async () => {
    vi.mocked(projectService.getDashboardStats).mockResolvedValue({
      projects: { total: 10, active: 5, draft: 2, approved: 3, rejected: 0 },
      repositories: { connected: 8, pending: 1, completed: 7, failed: 0 },
      compliance: { passing: 4, failed: 1 },
      security: { critical: 2, high: 5, open: 12 },
      recent_activity: []
    });

    render(<BrowserRouter><Dashboard /></BrowserRouter>);
    
    await waitFor(() => {
      expect(screen.getByText('Dashboard')).toBeInTheDocument();
    });

    expect(screen.getByText('10')).toBeInTheDocument(); // total projects
    expect(screen.getByText('12')).toBeInTheDocument(); // open security
  });
});
""",
    "pages/ProjectList.test.tsx": """
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
"""
}

for rel_path, content in TEST_FILES.items():
    write_file(os.path.join(BASE, rel_path), content)

print("Tests generated successfully!")
