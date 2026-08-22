import api from './api';
import type { RepositoryConnection, AnalysisSnapshot, TrainPlexReadiness } from '../types/repository';

export const repositoryService = {
  getConnections: async (): Promise<{ results: RepositoryConnection[] }> => {
    const response = await api.get('/repositories/connections/');
    return response.data;
  },
  getConnection: async (id: string): Promise<RepositoryConnection> => {
    const response = await api.get(`/repositories/connections/${id}/`);
    return response.data;
  },
  connectRepository: async (data: any): Promise<RepositoryConnection> => {
    const response = await api.post('/repositories/connections/', data);
    return response.data;
  },
  syncRepository: async (id: string): Promise<any> => {
    const response = await api.post(`/repositories/connections/${id}/sync/`);
    return response.data;
  },
  getLatestSnapshot: async (id: string): Promise<AnalysisSnapshot> => {
    const response = await api.get(`/repositories/connections/${id}/latest_snapshot/`);
    return response.data;
  },
  getTrainPlexReadiness: async (id: string): Promise<TrainPlexReadiness> => {
    const response = await api.get(`/repositories/connections/${id}/trainplex_readiness/`);
    return response.data;
  }
};
