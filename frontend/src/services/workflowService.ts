import api from './api';
import type { WorkflowDashboardData } from '../types/workflow';

export const workflowService = {
  getData: async (): Promise<{ results: WorkflowDashboardData[] }> => {
    const response = await api.get('/workflow/');
    return response.data;
  }
};
