import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { PublicLayout } from './layouts/PublicLayout';
import { AuthenticatedLayout } from './layouts/AuthenticatedLayout';
import { Login } from './pages/Login';
import { Dashboard } from './pages/Dashboard';
import { ProjectList } from './pages/ProjectList';
import { ProjectDetail } from './pages/ProjectDetail';
import { ProjectCreate } from './pages/ProjectCreate';
import { RepositoryList } from './pages/RepositoryList';
import { RepositoryConnect } from './pages/RepositoryConnect';
import { RepositoryDetail } from './pages/RepositoryDetail';
import { ComplianceDashboard } from './pages/ComplianceDashboard';
import { ComplianceRules } from './pages/ComplianceRules';
import { EvaluationDetail } from './pages/EvaluationDetail';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route element={<PublicLayout />}>
            <Route path="/login" element={<Login />} />
          </Route>
          
          <Route element={<AuthenticatedLayout />}>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/projects" element={<ProjectList />} />
            <Route path="/projects/new" element={<ProjectCreate />} />
            <Route path="/projects/:id" element={<ProjectDetail />} />
            
            <Route path="/repositories" element={<RepositoryList />} />
            <Route path="/repositories/connect" element={<RepositoryConnect />} />
            <Route path="/repositories/:id" element={<RepositoryDetail />} />
            
            <Route path="/compliance" element={<ComplianceDashboard />} />
            <Route path="/compliance/rules" element={<ComplianceRules />} />
            <Route path="/compliance/evaluations/:id" element={<EvaluationDetail />} />
            
            <Route path="/admin" element={<div>Admin (WIP)</div>} />
          </Route>

          <Route path="/" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
