import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { SecurityDashboard } from './SecurityDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/securityService', () => ({
  securityService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('SecurityDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><SecurityDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('SecurityDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><SecurityDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
