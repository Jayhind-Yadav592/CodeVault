import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

BASE = r"c:\Users\admin\Documents\TrainPlex\CodeVault\frontend"

FILES = {
    # .env files
    ".env.example": "VITE_API_BASE_URL=http://localhost:8000/api/v1\nVITE_APP_NAME=CodeVault",
    ".env.development.example": "VITE_API_BASE_URL=http://localhost:8000/api/v1\nVITE_APP_NAME=CodeVault",
    ".env.production.example": "VITE_API_BASE_URL=/api/v1\nVITE_APP_NAME=CodeVault",
    ".env": "VITE_API_BASE_URL=http://localhost:8000/api/v1\nVITE_APP_NAME=CodeVault",
    
    # Tailwind config
    "tailwind.config.js": """
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
""",
    
    # Vite config
    "vite.config.ts": """
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
""",
    
    # API service
    "src/services/api.ts": """
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
    }
    return Promise.reject(error);
  }
);

export default api;
""",
    
    # authService
    "src/services/authService.ts": """
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
""",
    
    # AuthContext
    "src/context/AuthContext.tsx": """
import React, { createContext, useContext, useState, useEffect } from 'react';
import { authService } from '../services/authService';

interface User {
  id: string;
  email: string;
  is_staff: boolean;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (credentials: any) => Promise<void>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      try {
        const currentUser = await authService.getCurrentUser();
        setUser(currentUser);
      } catch (error) {
        setUser(null);
      } finally {
        setLoading(false);
      }
    };
    initAuth();
  }, []);

  const login = async (credentials: any) => {
    await authService.login(credentials);
    const currentUser = await authService.getCurrentUser();
    setUser(currentUser);
  };

  const logout = async () => {
    await authService.logout();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
""",
    
    # Types
    "src/types/index.ts": """
export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
}

export interface Project {
  id: string;
  name: string;
  description: string;
}
""",
    
    # Design System - Button
    "src/components/ui/Button.tsx": """
import React from 'react';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger';
  isLoading?: boolean;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'primary', isLoading, children, ...props }, ref) => {
    const baseStyles = 'px-4 py-2 rounded font-medium focus:outline-none transition-colors';
    const variants = {
      primary: 'bg-blue-600 text-white hover:bg-blue-700',
      secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
      danger: 'bg-red-600 text-white hover:bg-red-700',
    };

    return (
      <button
        ref={ref}
        className={cn(baseStyles, variants[variant], className, isLoading && 'opacity-50 cursor-not-allowed')}
        disabled={isLoading || props.disabled}
        {...props}
      >
        {isLoading ? 'Loading...' : children}
      </button>
    );
  }
);
Button.displayName = 'Button';
""",
    
    # Layouts
    "src/layouts/PublicLayout.tsx": """
import React from 'react';
import { Outlet } from 'react-router-dom';

export const PublicLayout: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-center mb-6">{import.meta.env.VITE_APP_NAME || 'CodeVault'}</h1>
        <Outlet />
      </div>
    </div>
  );
};
""",
    
    "src/layouts/AuthenticatedLayout.tsx": """
import React from 'react';
import { Outlet, Navigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export const AuthenticatedLayout: React.FC = () => {
  const { user, loading, logout } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <Navigate to="/login" replace />;

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-white shadow-sm px-6 py-3 flex justify-between items-center">
        <div className="font-bold text-xl">CodeVault</div>
        <div className="flex gap-4 items-center">
          <span>{user.email}</span>
          <button onClick={logout} className="text-sm text-red-600 hover:underline">Logout</button>
        </div>
      </nav>
      <div className="flex">
        <aside className="w-64 bg-white min-h-[calc(100vh-60px)] border-r">
          <ul className="p-4 space-y-2">
            <li><Link to="/dashboard" className="block p-2 hover:bg-gray-50 rounded">Dashboard</Link></li>
            <li><Link to="/projects" className="block p-2 hover:bg-gray-50 rounded">Projects</Link></li>
          </ul>
        </aside>
        <main className="flex-1 p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
""",
    
    # Pages
    "src/pages/Login.tsx": """
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Button } from '../components/ui/Button';

export const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      await login({ email, password });
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.response?.data?.error || 'Login failed');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {error && <div className="p-3 bg-red-100 text-red-700 rounded text-sm">{error}</div>}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
        <input 
          type="email" 
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full border rounded p-2"
          required
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
        <input 
          type="password" 
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full border rounded p-2"
          required
        />
      </div>
      <Button type="submit" className="w-full">Sign In</Button>
    </form>
  );
};
""",
    
    "src/pages/Dashboard.tsx": """
import React from 'react';

export const Dashboard: React.FC = () => {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <div className="bg-white p-6 rounded-lg shadow-sm">
        <p className="text-gray-500">Welcome to your CodeVault dashboard. No data available yet.</p>
      </div>
    </div>
  );
};
""",
    
    # App.tsx
    "src/App.tsx": """
import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { PublicLayout } from './layouts/PublicLayout';
import { AuthenticatedLayout } from './layouts/AuthenticatedLayout';
import { Login } from './pages/Login';
import { Dashboard } from './pages/Dashboard';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route element={<PublicLayout />}>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<div>Register (WIP)</div>} />
          </Route>
          
          <Route element={<AuthenticatedLayout />}>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/projects" element={<div>Projects (WIP)</div>} />
            <Route path="/admin" element={<div>Admin (WIP)</div>} />
          </Route>

          <Route path="/" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
""",
    
    # main.tsx
    "src/main.tsx": """
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
""",
    
    # index.css
    "src/index.css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
""",
    
    # Vitest Config
    "vitest.config.ts": """
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    globals: true
  },
})
""",
    
    # Test Setup
    "src/test/setup.ts": """
import '@testing-library/jest-dom'
""",
    
    # Example Test
    "src/components/ui/Button.test.tsx": """
import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import { Button } from './Button'

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })
})
"""
}

for rel_path, content in FILES.items():
    write_file(os.path.join(BASE, rel_path), content)

print("Frontend files generated successfully!")
