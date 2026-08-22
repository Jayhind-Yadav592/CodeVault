import api from './api';
import type { SecurityDashboardData } from '../types/security';

export const securityService = {
  getData: async (): Promise<{ results: SecurityDashboardData[] }> => {
    const response = await api.get('/security/');
    return response.data;
  }
};
