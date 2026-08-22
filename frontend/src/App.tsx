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
import { SecurityDashboard } from './pages/SecurityDashboard';
import { ReviewCenter } from './pages/ReviewCenter';
import { LicensingDashboard } from './pages/LicensingDashboard';
import { MarketplaceDashboard } from './pages/MarketplaceDashboard';
import { FinanceDashboard } from './pages/FinanceDashboard';
import { AnalyticsDashboard } from './pages/AnalyticsDashboard';
import { GovernanceDashboard } from './pages/GovernanceDashboard';
import { WorkflowDashboard } from './pages/WorkflowDashboard';
import { IncidentDashboard } from './pages/IncidentDashboard';

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
            <Route path="/security" element={<SecurityDashboard />} />
            <Route path="/review" element={<ReviewCenter />} />
            <Route path="/licensing" element={<LicensingDashboard />} />
            <Route path="/marketplace" element={<MarketplaceDashboard />} />
            <Route path="/finance" element={<FinanceDashboard />} />
            <Route path="/analytics" element={<AnalyticsDashboard />} />
            <Route path="/governance" element={<GovernanceDashboard />} />
            <Route path="/workflow" element={<WorkflowDashboard />} />
            <Route path="/incident" element={<IncidentDashboard />} />
            
            <Route path="/admin" element={<div>Admin (WIP)</div>} />
          </Route>

          <Route path="/" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
