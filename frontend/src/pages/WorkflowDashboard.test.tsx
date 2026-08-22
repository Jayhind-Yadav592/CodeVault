import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { WorkflowDashboard } from './WorkflowDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/workflowService', () => ({
  workflowService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('WorkflowDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><WorkflowDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('WorkflowDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><WorkflowDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
