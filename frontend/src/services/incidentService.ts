import api from './api';
import type { IncidentDashboardData } from '../types/incident';

export const incidentService = {
  getData: async (): Promise<{ results: IncidentDashboardData[] }> => {
    const response = await api.get('/incident/');
    return response.data;
  }
};
