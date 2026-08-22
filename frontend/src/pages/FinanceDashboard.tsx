import { useEffect, useState } from 'react';
import { financeService } from '../services/financeService';
import type { FinanceTransaction } from '../types/finance';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Button } from '../components/ui/Button';
import { DollarSign } from 'lucide-react';

export const FinanceDashboard = () => {
  const [transactions, setTransactions] = useState<FinanceTransaction[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchTransactions = async () => {
    setLoading(true);
    try {
      const data = await financeService.getTransactions();
      setTransactions(data.results || []);
    } catch (err: any) {
      setError(err.response?.data?.details || 'Failed to load financial transactions');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  return (
    <div className="space-y-8 max-w-7xl mx-auto">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <DollarSign className="w-8 h-8 text-[#0052D4]" /> Finance
        </h1>
        <Button variant="primary" onClick={fetchTransactions}>Refresh Ledger</Button>
      </div>

      {error && <div className="p-4 bg-red-50 text-red-700 border border-red-200 rounded-xl">{error}</div>}

      <div className="bg-white shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] rounded-[18px] border border-slate-200 overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow>
              <TableCell isHeader>Tx ID</TableCell>
              <TableCell isHeader>Type</TableCell>
              <TableCell isHeader>Status</TableCell>
              <TableCell isHeader>Currency</TableCell>
              <TableCell isHeader>Description</TableCell>
              <TableCell isHeader>Date</TableCell>
            </TableRow>
          </TableHeader>
          <tbody>
            {loading ? (
              <TableRow><TableCell colSpan={6} className="text-center py-8">Loading ledger...</TableCell></TableRow>
            ) : transactions.length === 0 ? (
              <TableRow>
                <TableCell colSpan={6} className="text-center py-12 text-slate-500">
                  No financial transactions found.
                </TableCell>
              </TableRow>
            ) : (
              transactions.map(t => (
                <TableRow key={t.id}>
                  <TableCell className="font-mono text-xs text-slate-500">{t.id.split('-')[0]}</TableCell>
                  <TableCell className="uppercase text-xs font-bold text-slate-600">{t.transaction_type}</TableCell>
                  <TableCell>
                    <span className="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-md uppercase">
                      {t.status}
                    </span>
                  </TableCell>
                  <TableCell className="font-bold">{t.currency}</TableCell>
                  <TableCell>{t.description}</TableCell>
                  <TableCell>{new Date(t.created_at).toLocaleDateString()}</TableCell>
                </TableRow>
              ))
            )}
          </tbody>
        </Table>
      </div>
    </div>
  );
};
