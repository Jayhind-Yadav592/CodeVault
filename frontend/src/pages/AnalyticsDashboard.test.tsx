import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { AnalyticsDashboard } from './AnalyticsDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/analyticsService', () => ({
  analyticsService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('AnalyticsDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><AnalyticsDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('AnalyticsDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><AnalyticsDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
