import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { GovernanceDashboard } from './GovernanceDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/governanceService', () => ({
  governanceService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('GovernanceDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><GovernanceDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('GovernanceDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><GovernanceDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
