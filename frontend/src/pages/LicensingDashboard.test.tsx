import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { LicensingDashboard } from './LicensingDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/licensingService', () => ({
  licensingService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('LicensingDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><LicensingDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('LicensingDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><LicensingDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
