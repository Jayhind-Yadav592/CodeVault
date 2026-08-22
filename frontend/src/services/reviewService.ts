import api from './api';
import type { ReviewCase } from '../types/review';

export const reviewService = {
  getCases: async (): Promise<{ results: ReviewCase[] }> => {
    const response = await api.get('/reviews/cases/');
    return response.data;
  },
  transitionCase: async (id: string, newState: string, reason?: string): Promise<any> => {
    const response = await api.post(`/reviews/cases/${id}/transition/`, { new_state: newState, reason });
    return response.data;
  }
};
