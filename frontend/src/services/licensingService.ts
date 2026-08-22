import api from './api';
import type { LicenseAgreement, LicenseRequest } from '../types/licensing';

export const licensingService = {
  getAgreements: async (): Promise<{ results: LicenseAgreement[] }> => {
    const response = await api.get('/licensing/agreements/');
    return response.data;
  },
  getRequests: async (): Promise<{ results: LicenseRequest[] }> => {
    const response = await api.get('/licensing/requests/');
    return response.data;
  }
};
