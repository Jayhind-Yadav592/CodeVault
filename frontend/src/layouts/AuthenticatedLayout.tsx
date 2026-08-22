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
