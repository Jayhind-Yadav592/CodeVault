import api from './api';
import type { AnalyticsDashboardData } from '../types/analytics';

export const analyticsService = {
  getData: async (): Promise<{ results: AnalyticsDashboardData[] }> => {
    const response = await api.get('/analytics/');
    return response.data;
  }
};
