import api from './api';
import type { GovernanceDashboardData } from '../types/governance';

export const governanceService = {
  getData: async (): Promise<{ results: GovernanceDashboardData[] }> => {
    const response = await api.get('/governance/');
    return response.data;
  }
};
