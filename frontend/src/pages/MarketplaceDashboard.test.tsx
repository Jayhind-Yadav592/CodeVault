import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { MarketplaceDashboard } from './MarketplaceDashboard';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/marketplaceService', () => ({
  marketplaceService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('MarketplaceDashboard', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><MarketplaceDashboard /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('MarketplaceDashboard')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><MarketplaceDashboard /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
