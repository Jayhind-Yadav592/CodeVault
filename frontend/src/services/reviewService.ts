import api from './api';
import type { ReviewCenterData } from '../types/review';

export const reviewService = {
  getData: async (): Promise<{ results: ReviewCenterData[] }> => {
    const response = await api.get('/review/');
    return response.data;
  }
};
