
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
