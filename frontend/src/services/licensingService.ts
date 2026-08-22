import api from './api';
import type { LicensingDashboardData } from '../types/licensing';

export const licensingService = {
  getData: async (): Promise<{ results: LicensingDashboardData[] }> => {
    const response = await api.get('/licensing/licenseagreements/');
    return response.data;
  }
};
