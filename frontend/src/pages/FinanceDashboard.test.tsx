import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { FinanceDashboard } from './FinanceDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/financeService', () => ({
  financeService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('FinanceDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><FinanceDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('FinanceDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><FinanceDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
