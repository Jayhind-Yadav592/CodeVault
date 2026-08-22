import api from './api';
import type { FinanceDashboardData } from '../types/finance';

export const financeService = {
  getData: async (): Promise<{ results: FinanceDashboardData[] }> => {
    const response = await api.get('/finance/transactions/');
    return response.data;
  }
};
