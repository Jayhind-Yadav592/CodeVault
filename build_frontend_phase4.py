import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

BASE = r"c:\Users\admin\Documents\TrainPlex\CodeVault\frontend\src"

FILES = {
    # Types
    "types/compliance.ts": """
export interface ComplianceDashboard {
  total: number;
  passing: number;
  failed: number;
  partial: number;
  unknown: number;
  manual_review: number;
  recent: Array<{ id: string; decision: string; project: string; date: string }>;
}

export interface ComplianceRule {
  id: string;
  rule_id: string;
  name: string;
  category: string;
  severity: string;
  description: string;
}

export interface ComplianceEvaluation {
  id: string;
  decision: string;
  created_at: string;
  overall_score: number;
  rules: Array<{
    rule_id: string;
    name: string;
    category: string;
    severity: string;
    status: string;
    evidence: any;
    is_critical_failure: boolean;
  }>;
}
""",

    # Service
    "services/complianceService.ts": """
import api from './api';
import type { ComplianceDashboard, ComplianceRule, ComplianceEvaluation } from '../types/compliance';

export const complianceService = {
  getDashboard: async (): Promise<ComplianceDashboard> => {
    const response = await api.get('/compliance/evaluations/dashboard/');
    return response.data;
  },
  getRules: async (): Promise<{ results: ComplianceRule[] }> => {
    const response = await api.get('/compliance/rules/');
    return response.data;
  },
  getEvaluationDetails: async (id: string): Promise<ComplianceEvaluation> => {
    const response = await api.get(`/compliance/evaluations/${id}/details/`);
    return response.data;
  }
};
""",

    # Compliance Dashboard Page
    "pages/ComplianceDashboard.tsx": """
import { useEffect, useState } from 'react';
import { complianceService } from '../services/complianceService';
import type { ComplianceDashboard as CDashboard } from '../types/compliance';
import { LoadingState } from '../components/ui/LoadingState';
import { Card, CardContent, CardHeader } from '../components/ui/Card';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Badge } from '../components/ui/Badge';

export const ComplianceDashboard = () => {
  const [data, setData] = useState<CDashboard | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    complianceService.getDashboard()
      .then(setData)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingState />;
  if (!data) return <div>Error loading compliance data</div>;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Compliance Dashboard</h1>
      
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        <Card><CardHeader>Total</CardHeader><CardContent className="text-2xl font-bold">{data.total}</CardContent></Card>
        <Card><CardHeader>Passing</CardHeader><CardContent className="text-2xl font-bold text-green-600">{data.passing}</CardContent></Card>
        <Card><CardHeader>Failed</CardHeader><CardContent className="text-2xl font-bold text-red-600">{data.failed}</CardContent></Card>
        <Card><CardHeader>Partial</CardHeader><CardContent className="text-2xl font-bold text-yellow-600">{data.partial}</CardContent></Card>
        <Card><CardHeader>Manual</CardHeader><CardContent className="text-2xl font-bold text-blue-600">{data.manual_review}</CardContent></Card>
        <Card><CardHeader>Unknown</CardHeader><CardContent className="text-2xl font-bold text-gray-500">{data.unknown}</CardContent></Card>
      </div>

      <Card>
        <CardHeader>Recent Evaluations</CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableCell isHeader>Project</TableCell>
                <TableCell isHeader>Date</TableCell>
                <TableCell isHeader>Decision</TableCell>
                <TableCell isHeader>Actions</TableCell>
              </TableRow>
            </TableHeader>
            <tbody>
              {data.recent.map(r => (
                <TableRow key={r.id}>
                  <TableCell>{r.project}</TableCell>
                  <TableCell>{new Date(r.date).toLocaleString()}</TableCell>
                  <TableCell><Badge>{r.decision}</Badge></TableCell>
                  <TableCell>
                    <a href={`/compliance/evaluations/${r.id}`} className="text-blue-600 hover:underline">View</a>
                  </TableCell>
                </TableRow>
              ))}
              {data.recent.length === 0 && <TableRow><TableCell colSpan={4}>No recent evaluations.</TableCell></TableRow>}
            </tbody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
};
""",

    # Rules Page
    "pages/ComplianceRules.tsx": """
import { useEffect, useState } from 'react';
import { complianceService } from '../services/complianceService';
import type { ComplianceRule } from '../types/compliance';
import { LoadingState } from '../components/ui/LoadingState';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Badge } from '../components/ui/Badge';

export const ComplianceRules = () => {
  const [rules, setRules] = useState<ComplianceRule[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    complianceService.getRules()
      .then(d => setRules(d.results || (d as any)))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingState />;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Compliance Rule Registry</h1>
      
      <div className="bg-white shadow rounded">
        <Table>
          <TableHeader>
            <TableRow>
              <TableCell isHeader>Rule ID</TableCell>
              <TableCell isHeader>Name</TableCell>
              <TableCell isHeader>Category</TableCell>
              <TableCell isHeader>Severity</TableCell>
            </TableRow>
          </TableHeader>
          <tbody>
            {rules.map(r => (
              <TableRow key={r.id}>
                <TableCell className="font-mono text-sm">{r.rule_id}</TableCell>
                <TableCell>
                  <div className="font-medium">{r.name}</div>
                  <div className="text-sm text-gray-500">{r.description}</div>
                </TableCell>
                <TableCell><Badge variant="default">{r.category}</Badge></TableCell>
                <TableCell><Badge variant={r.severity === 'critical' ? 'danger' : r.severity === 'warning' ? 'warning' : 'success'}>{r.severity}</Badge></TableCell>
              </TableRow>
            ))}
          </tbody>
        </Table>
      </div>
    </div>
  );
};
""",

    # Evaluation Details Page
    "pages/EvaluationDetail.tsx": """
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { complianceService } from '../services/complianceService';
import type { ComplianceEvaluation } from '../types/compliance';
import { LoadingState } from '../components/ui/LoadingState';
import { Card, CardContent, CardHeader } from '../components/ui/Card';
import { Badge } from '../components/ui/Badge';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';

export const EvaluationDetail = () => {
  const { id } = useParams<{ id: string }>();
  const [evalData, setEvalData] = useState<ComplianceEvaluation | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (id) {
      complianceService.getEvaluationDetails(id)
        .then(setEvalData)
        .catch(console.error)
        .finally(() => setLoading(false));
    }
  }, [id]);

  if (loading) return <LoadingState />;
  if (!evalData) return <div>Evaluation not found</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center border-b pb-4">
        <div>
          <h1 className="text-3xl font-bold mb-1">Compliance Evaluation</h1>
          <span className="text-gray-500">ID: {evalData.id}</span>
        </div>
        <div className="flex items-center gap-2">
          <span>Decision: </span>
          <Badge variant={evalData.decision === 'eligible' ? 'success' : evalData.decision === 'ineligible' ? 'danger' : 'warning'}>
            {evalData.decision.replace(/_/g, ' ').toUpperCase()}
          </Badge>
        </div>
      </div>

      <Card>
        <CardHeader>Technical & Legal Rules Executed</CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableCell isHeader>Rule</TableCell>
                <TableCell isHeader>Category</TableCell>
                <TableCell isHeader>Status</TableCell>
                <TableCell isHeader>Evidence</TableCell>
              </TableRow>
            </TableHeader>
            <tbody>
              {evalData.rules.map((r, idx) => (
                <TableRow key={idx}>
                  <TableCell>
                    <div className="font-medium">{r.name}</div>
                    <div className="text-xs text-gray-500">{r.rule_id}</div>
                  </TableCell>
                  <TableCell>{r.category}</TableCell>
                  <TableCell>
                    <Badge variant={r.status === 'pass' ? 'success' : r.status === 'fail' ? 'danger' : 'warning'}>
                      {r.status.toUpperCase()}
                    </Badge>
                  </TableCell>
                  <TableCell className="font-mono text-xs overflow-hidden max-w-xs truncate">
                    {JSON.stringify(r.evidence)}
                  </TableCell>
                </TableRow>
              ))}
            </tbody>
          </Table>
        </CardContent>
      </Card>
      
      {evalData.decision === 'requires_human_review' && (
        <Card>
          <CardHeader>Manual Review Required</CardHeader>
          <CardContent>
            <p className="text-gray-600">This project cannot be automatically approved due to intellectual property checks, fork detection, or manual ownership verification rules.</p>
            <button className="mt-4 bg-blue-600 text-white px-4 py-2 rounded">Assign to Reviewer</button>
          </CardContent>
        </Card>
      )}
    </div>
  );
};
""",

    # Add to App.tsx
    "App.tsx": """
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
""",

    # Update AuthenticatedLayout Sidebar
    "layouts/AuthenticatedLayout.tsx": """
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
          </ul>
        </aside>
        <main className="flex-1 p-8 overflow-y-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
"""
}

for rel_path, content in FILES.items():
    write_file(os.path.join(BASE, rel_path), content)

print("Phase 4 components and pages generated successfully!")
