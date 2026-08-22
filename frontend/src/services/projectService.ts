import api from './api';
import type { Project, DashboardData } from '../types/project';

export const projectService = {
  getDashboardStats: async (): Promise<DashboardData> => {
    const response = await api.get('/projects/dashboard/');
    return response.data;
  },
  getProjects: async (params?: any): Promise<{ results: Project[], count: number }> => {
    const response = await api.get('/projects/', { params });
    return response.data;
  },
  getProject: async (id: string): Promise<Project> => {
    const response = await api.get(`/projects/${id}/`);
    return response.data;
  },
  createProject: async (data: any): Promise<Project> => {
    const response = await api.post('/projects/', data);
    return response.data;
  }
};
