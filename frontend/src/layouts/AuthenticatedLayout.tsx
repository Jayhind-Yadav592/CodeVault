import { Outlet, Navigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export const AuthenticatedLayout = () => {
  const { user, loading, logout } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <Navigate to="/login" replace />;

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <nav className="bg-blue-900 text-white shadow-sm px-6 py-3 flex justify-between items-center">
        <div className="font-bold text-xl tracking-wider">CODEVAULT</div>
        <div className="flex gap-4 items-center">
          <span className="text-sm opacity-80">{user.email}</span>
          <button onClick={logout} className="text-sm bg-blue-800 px-3 py-1 rounded hover:bg-blue-700 transition">Logout</button>
        </div>
      </nav>
      <div className="flex flex-1">
        <aside className="w-64 bg-white shadow-md border-r border-gray-200">
          <ul className="p-4 space-y-2">
            <li><Link to="/dashboard" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Dashboard</Link></li>
            <li><Link to="/projects" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Projects</Link></li>
            <li><Link to="/repositories" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Repositories</Link></li>
            <div className="pt-4 pb-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">Compliance</div>
            <li><Link to="/compliance" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Dashboard</Link></li>
            <li><Link to="/compliance/rules" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Rule Registry</Link></li>
            <li><Link to="/security" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Security</Link></li>
            <li><Link to="/review" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Review</Link></li>
            <li><Link to="/licensing" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Licensing</Link></li>
            <li><Link to="/marketplace" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Marketplace</Link></li>
            <li><Link to="/finance" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Finance</Link></li>
            <li><Link to="/analytics" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Analytics</Link></li>
            <li><Link to="/governance" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Governance</Link></li>
            <li><Link to="/workflow" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Workflow</Link></li>
            <li><Link to="/incident" className="block p-2 hover:bg-blue-50 text-gray-700 hover:text-blue-700 rounded font-medium">Incident</Link></li>
          </ul>
        </aside>
        <main className="flex-1 p-8 overflow-y-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
