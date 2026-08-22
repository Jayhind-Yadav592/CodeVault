import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { RepositoryList } from './RepositoryList';
import { repositoryService } from '../services/repositoryService';
import { BrowserRouter } from 'react-router-dom';

vi.mock('../services/repositoryService');

describe('RepositoryList', () => {
  it('renders correctly with empty data', async () => {
    vi.mocked(repositoryService.getConnections).mockResolvedValue({ results: [] });

    render(<BrowserRouter><RepositoryList /></BrowserRouter>);
    
    await waitFor(() => {
      expect(screen.getByText('Repositories')).toBeInTheDocument();
    });
    
    expect(screen.getByText('No repositories connected.')).toBeInTheDocument();
  });
});
