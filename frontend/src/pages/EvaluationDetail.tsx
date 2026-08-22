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
          <span className="text-gray-900">ID: {evalData.id}</span>
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
                    <div className="text-xs text-gray-900">{r.rule_id}</div>
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
