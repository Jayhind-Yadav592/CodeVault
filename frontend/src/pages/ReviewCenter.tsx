import { useEffect, useState } from 'react';
import { reviewService } from '../services/reviewService';
import type { ReviewCase } from '../types/review';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Button } from '../components/ui/Button';
import { CheckSquare } from 'lucide-react';

export const ReviewCenter = () => {
  const [cases, setCases] = useState<ReviewCase[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchCases = async () => {
    setLoading(true);
    try {
      const data = await reviewService.getCases();
      setCases(data.results || []);
    } catch (err: any) {
      setError(err.response?.data?.details || 'Failed to load review cases');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCases();
  }, []);

  const getStateColor = (state: string) => {
    if (state === 'approved') return 'bg-emerald-100 text-emerald-700';
    if (state === 'rejected') return 'bg-red-100 text-red-700';
    if (state === 'draft' || state === 'submitted') return 'bg-slate-100 text-slate-700';
    return 'bg-blue-100 text-blue-700';
  };

  return (
    <div className="space-y-8 max-w-7xl mx-auto">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <CheckSquare className="w-8 h-8 text-[#0052D4]" /> Review Center
        </h1>
        <Button variant="primary" onClick={fetchCases}>Refresh Reviews</Button>
      </div>

      {error && <div className="p-4 bg-red-50 text-red-700 border border-red-200 rounded-xl">{error}</div>}

      <div className="bg-white shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] rounded-[18px] border border-slate-200 overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow>
              <TableCell isHeader>Review ID</TableCell>
              <TableCell isHeader>Project Reference</TableCell>
              <TableCell isHeader>State</TableCell>
              <TableCell isHeader>Priority</TableCell>
              <TableCell isHeader>Due Date</TableCell>
            </TableRow>
          </TableHeader>
          <tbody>
            {loading ? (
              <TableRow><TableCell colSpan={5} className="text-center py-8">Loading review cases...</TableCell></TableRow>
            ) : cases.length === 0 ? (
              <TableRow>
                <TableCell colSpan={5} className="text-center py-12 text-slate-500">
                  No pending reviews. <br/>
                  <span className="text-sm mt-2 block">Submit a project for review to see it here.</span>
                </TableCell>
              </TableRow>
            ) : (
              cases.map(c => (
                <TableRow key={c.id}>
                  <TableCell className="font-mono text-xs text-slate-500">{c.id.split('-')[0]}</TableCell>
                  <TableCell className="font-medium text-slate-900">{c.project}</TableCell>
                  <TableCell>
                    <span className={`px-2 py-1 rounded text-xs font-semibold uppercase tracking-wider ${getStateColor(c.state)}`}>
                      {c.state.replace('_', ' ')}
                    </span>
                  </TableCell>
                  <TableCell className="uppercase text-xs font-semibold text-slate-600">{c.priority}</TableCell>
                  <TableCell>{c.due_date ? new Date(c.due_date).toLocaleDateString() : 'N/A'}</TableCell>
                </TableRow>
              ))
            )}
          </tbody>
        </Table>
      </div>
    </div>
  );
};
