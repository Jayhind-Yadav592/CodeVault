import api from './api';
import type { Finding, SecurityScanJob } from '../types/security';

export const securityService = {
  getFindings: async (): Promise<{ results: Finding[] }> => {
    const response = await api.get('/security/findings/');
    return response.data;
  },
  getScanJobs: async (): Promise<{ results: SecurityScanJob[] }> => {
    const response = await api.get('/security/jobs/');
    return response.data;
  },
  triggerScan: async (snapshotId: string): Promise<any> => {
    const response = await api.post('/security/jobs/trigger/', { snapshot_id: snapshotId });
    return response.data;
  },
  updateFindingStatus: async (findingId: string, status: string, note?: string): Promise<any> => {
    const response = await api.post(`/security/findings/${findingId}/update_status/`, { status, note });
    return response.data;
  }
};
