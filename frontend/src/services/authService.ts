import api from './api';

export const authService = {
  login: async (credentials: any) => {
    const response = await api.post('/accounts/login/', credentials);
    if (response.data && response.data.access) {
        localStorage.setItem('access_token', response.data.access);
    }
    return response.data;
  },
  logout: async () => {
    localStorage.removeItem('access_token');
    try {
        const response = await api.post('/accounts/logout/');
        return response.data;
    } catch {
        return null; // logout endpoint might not exist in simplejwt by default
    }
  },
  getCurrentUser: async () => {
    const response = await api.get('/accounts/profile/');
    return response.data;
  }
};
