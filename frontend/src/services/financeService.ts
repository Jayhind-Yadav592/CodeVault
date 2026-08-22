import api from './api';
import type { FinanceTransaction } from '../types/finance';

export const financeService = {
  getTransactions: async (): Promise<{ results: FinanceTransaction[] }> => {
    const response = await api.get('/finance/transactions/');
    return response.data;
  }
};
