import api from './api';

export const authService = {
  login: async (credentials: any) => {
    // Assuming backend returns a token or sets a session cookie
    const response = await api.post('/auth/login/', credentials);
    return response.data;
  },
  logout: async () => {
    const response = await api.post('/auth/logout/');
    return response.data;
  },
  getCurrentUser: async () => {
    const response = await api.get('/auth/user/');
    return response.data;
  }
};
