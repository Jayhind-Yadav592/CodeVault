import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { ReviewCenter } from './ReviewCenter';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/reviewService', () => ({
  reviewService: {
    getData: vi.fn().mockResolvedValue({ results: [] })
  }
}));

describe('ReviewCenter', () => {
  it('renders correctly', async () => {
    render(<BrowserRouter><ReviewCenter /></BrowserRouter>);
    await waitFor(() => {
      expect(screen.getByText('ReviewCenter')).toBeInTheDocument();
      expect(screen.getByText(/No records/i)).toBeInTheDocument();
    });
  });
  
  it('handles loading state', () => {
    render(<BrowserRouter><ReviewCenter /></BrowserRouter>);
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();
  });
});
