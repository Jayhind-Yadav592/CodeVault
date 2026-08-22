import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { IncidentDashboard } from './IncidentDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/incidentService', () => ({
  incidentService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('IncidentDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><IncidentDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('IncidentDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><IncidentDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
