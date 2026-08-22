import api from './api';
import type { MarketplaceDashboardData } from '../types/marketplace';

export const marketplaceService = {
  getData: async (): Promise<{ results: MarketplaceDashboardData[] }> => {
    const response = await api.get('/marketplace/marketplacelistings/');
    return response.data;
  }
};
