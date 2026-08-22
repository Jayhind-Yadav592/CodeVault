import api from './api';
import type { ComplianceDashboard, ComplianceRule, ComplianceEvaluation } from '../types/compliance';

export const complianceService = {
  getDashboard: async (): Promise<ComplianceDashboard> => {
    const response = await api.get('/compliance/evaluations/dashboard/');
    return response.data;
  },
  getRules: async (): Promise<{ results: ComplianceRule[] }> => {
    const response = await api.get('/compliance/rules/');
    return response.data;
  },
  getEvaluationDetails: async (id: string): Promise<ComplianceEvaluation> => {
    const response = await api.get(`/compliance/evaluations/${id}/details/`);
    return response.data;
  }
};
