import api from './api';
import type { MarketplaceListing } from '../types/marketplace';

export const marketplaceService = {
  getListings: async (): Promise<{ results: MarketplaceListing[] }> => {
    const response = await api.get('/marketplace/listings/');
    return response.data;
  }
};
