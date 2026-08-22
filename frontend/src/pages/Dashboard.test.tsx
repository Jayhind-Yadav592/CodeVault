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
