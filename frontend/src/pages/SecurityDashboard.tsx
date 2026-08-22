import { useEffect, useState } from 'react';
import { securityService } from '../services/securityService';
import type { SecurityDashboardData } from '../types/security';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { LoadingState } from '../components/ui/LoadingState';

export const SecurityDashboard = () => {
  const [data, setData] = useState<SecurityDashboardData[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    securityService.getData().then(d => setData(d.results || (d as any))).catch(console.error).finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingState />;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">SecurityDashboard</h1>
      <div className="bg-white shadow rounded">
        <Table>
          <TableHeader>
            <TableRow>
              <TableCell isHeader>ID</TableCell>
              <TableCell isHeader>Name</TableCell>
              <TableCell isHeader>Status</TableCell>
            </TableRow>
          </TableHeader>
          <tbody>
            {data.map(item => (
              <TableRow key={item.id}>
                <TableCell>{item.id}</TableCell>
                <TableCell>{item.name}</TableCell>
                <TableCell>{item.status}</TableCell>
              </TableRow>
            ))}
            {data.length === 0 && <TableRow><TableCell colSpan={3}>No records found.</TableCell></TableRow>}
          </tbody>
        </Table>
      </div>
    </div>
  );
};
