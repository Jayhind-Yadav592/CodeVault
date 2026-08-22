import { useEffect, useState } from 'react';
import { securityService } from '../services/securityService';
import type { Finding, SecurityScanJob } from '../types/security';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Card, CardHeader, CardContent } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Shield, AlertTriangle, ShieldCheck, Activity } from 'lucide-react';

export const SecurityDashboard = () => {
  const [findings, setFindings] = useState<Finding[]>([]);
  const [jobs, setJobs] = useState<SecurityScanJob[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchData = async () => {
    setLoading(true);
    setError('');
    try {
      const [findingsData, jobsData] = await Promise.all([
        securityService.getFindings(),
        securityService.getScanJobs()
      ]);
      setFindings(findingsData.results || []);
      setJobs(jobsData.results || []);
    } catch (err: any) {
      setError(err.response?.data?.details || err.message || 'Failed to load security data.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const getSeverityColor = (severity: string) => {
    switch(severity) {
      case 'critical': return 'text-red-600 bg-red-100 border-red-200';
      case 'high': return 'text-orange-600 bg-orange-100 border-orange-200';
      case 'medium': return 'text-yellow-600 bg-yellow-100 border-yellow-200';
      case 'low': return 'text-blue-600 bg-blue-100 border-blue-200';
      default: return 'text-slate-600 bg-slate-100 border-slate-200';
    }
  };

  if (loading) {
    return <div className="flex h-[400px] items-center justify-center text-slate-500">Loading security findings...</div>;
  }

  const criticalCount = findings.filter(f => f.severity === 'critical' && f.status === 'open').length;
  const highCount = findings.filter(f => f.severity === 'high' && f.status === 'open').length;

  return (
    <div className="space-y-8 max-w-7xl mx-auto">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <Shield className="w-8 h-8 text-[#0052D4]" /> Security Center
        </h1>
        <Button variant="primary" onClick={fetchData}>Refresh Data</Button>
      </div>

      {error && <div className="p-4 bg-red-50 text-red-700 border border-red-200 rounded-xl">{error}</div>}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card gradientTop>
          <CardHeader>Open Critical Issues</CardHeader>
          <CardContent className="flex items-center gap-4">
            <AlertTriangle className={`w-10 h-10 ${criticalCount > 0 ? 'text-red-500' : 'text-slate-300'}`} />
            <span className="text-4xl font-bold text-slate-800">{criticalCount}</span>
          </CardContent>
        </Card>
        <Card gradientTop>
          <CardHeader>Open High Issues</CardHeader>
          <CardContent className="flex items-center gap-4">
            <Activity className={`w-10 h-10 ${highCount > 0 ? 'text-orange-500' : 'text-slate-300'}`} />
            <span className="text-4xl font-bold text-slate-800">{highCount}</span>
          </CardContent>
        </Card>
        <Card gradientTop>
          <CardHeader>Total Scans Performed</CardHeader>
          <CardContent className="flex items-center gap-4">
            <ShieldCheck className="w-10 h-10 text-emerald-500" />
            <span className="text-4xl font-bold text-slate-800">{jobs.length}</span>
          </CardContent>
        </Card>
      </div>

      <div className="space-y-4">
        <h2 className="text-xl font-bold text-slate-800">Security Findings</h2>
        <Table>
          <TableHeader>
            <TableRow>
              <TableCell isHeader>ID</TableCell>
              <TableCell isHeader>Severity</TableCell>
              <TableCell isHeader>Category</TableCell>
              <TableCell isHeader>Description</TableCell>
              <TableCell isHeader>Status</TableCell>
            </TableRow>
          </TableHeader>
          <tbody>
            {findings.length === 0 ? (
              <TableRow>
                <TableCell colSpan={5} className="text-center py-12 text-slate-500">
                  No security findings have been recorded yet. <br/>
                  <span className="text-sm mt-2 block">Connect a repository and run a scan to get started.</span>
                </TableCell>
              </TableRow>
            ) : (
              findings.map(finding => (
                <TableRow key={finding.id}>
                  <TableCell className="font-mono text-xs">{finding.id.split('-')[0]}</TableCell>
                  <TableCell>
                    <span className={`px-2.5 py-1 rounded-md text-xs font-bold border uppercase tracking-wider ${getSeverityColor(finding.severity)}`}>
                      {finding.severity}
                    </span>
                  </TableCell>
                  <TableCell className="uppercase tracking-wider text-xs font-semibold text-slate-600">{finding.category.replace('_', ' ')}</TableCell>
                  <TableCell className="max-w-md truncate" title={finding.short_description}>{finding.short_description}</TableCell>
                  <TableCell>
                    <span className="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-md uppercase">
                      {finding.status}
                    </span>
                  </TableCell>
                </TableRow>
              ))
            )}
          </tbody>
        </Table>
      </div>
    </div>
  );
};
