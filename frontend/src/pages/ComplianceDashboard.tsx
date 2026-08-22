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
