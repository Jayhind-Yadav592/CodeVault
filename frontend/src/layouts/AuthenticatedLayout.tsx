import { Outlet, Navigate, NavLink } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { LayoutDashboard, Folder, GitBranch, ShieldCheck, Lock, CheckSquare, FileText, ShoppingBag, DollarSign, Shield, LogOut, Bell } from 'lucide-react';
import { cn } from '../utils';

export const AuthenticatedLayout = () => {
  const { user, loading, logout } = useAuth();

  if (loading) return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  if (!user) return <Navigate to="/login" replace />;

  const navItems = [
    { to: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { to: '/projects', label: 'Projects', icon: Folder },
    { to: '/repositories', label: 'Repositories', icon: GitBranch },
    { to: '/compliance', label: 'Compliance', icon: ShieldCheck },
    { to: '/security', label: 'Security', icon: Lock },
    { to: '/review', label: 'Review Center', icon: CheckSquare },
    { to: '/licensing', label: 'Licensing', icon: FileText },
    { to: '/marketplace', label: 'Marketplace', icon: ShoppingBag },
    { to: '/finance', label: 'Finance', icon: DollarSign },

  ];

  return (
    <div className="min-h-screen flex font-sans bg-transparent">
      {/* Background Canvas */}
      <div className="bg-canvas">
        <div className="orb orb1"></div>
        <div className="orb orb2"></div>
        <div className="orb orb3"></div>
      </div>

      {/* Sidebar */}
      <aside className="w-[265px] bg-white/92 border-r border-gray-200/50 p-6 flex flex-col fixed top-0 left-0 h-screen z-50 backdrop-blur-md">
        <div className="flex items-center justify-center gap-2 text-slate-900 font-bold text-xl mb-8 pb-6 border-b border-gray-200/50">
          <Shield className="w-8 h-8 text-[#0052D4]" />
          CodeVault
        </div>

        <nav className="flex flex-col gap-1 flex-1 overflow-y-auto pr-2 custom-scrollbar">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) => cn(
                "flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 shrink-0",
                isActive 
                  ? "bg-blue-50/50 text-[#0052D4] font-semibold" 
                  : "text-slate-600 hover:bg-slate-50 hover:text-slate-900"
              )}
            >
              <item.icon className="w-5 h-5 shrink-0" />
              {item.label}
            </NavLink>
          ))}
        </nav>

        <div className="pt-4 mt-4 border-t border-gray-200/50">
          <button 
            onClick={logout} 
            className="flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-slate-600 hover:bg-red-50 hover:text-red-600 w-full transition-all duration-200"
          >
            <LogOut className="w-5 h-5" />
            Sign Out
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 ml-[265px] flex flex-col min-h-screen">
        {/* Top Navigation */}
        <header className="h-[72px] bg-transparent flex items-center justify-end px-8 sticky top-0 z-40">
          <div className="flex items-center gap-6 bg-white/60 backdrop-blur-md px-6 py-2.5 rounded-full border border-white shadow-sm">
            <span className="text-sm font-medium text-slate-700">Hello, {user.email}</span>
            <button className="relative text-slate-500 hover:text-[#0052D4] transition-colors">
              <Bell className="w-5 h-5" />
              <span className="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full border border-white"></span>
            </button>
          </div>
        </header>

        {/* Page Content */}
        <main className="flex-1 p-8 pt-4">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
