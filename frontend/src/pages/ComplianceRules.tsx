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
