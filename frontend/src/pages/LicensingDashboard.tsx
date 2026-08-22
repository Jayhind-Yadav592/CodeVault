import { useEffect, useState } from 'react';
import { licensingService } from '../services/licensingService';
import type { LicenseAgreement } from '../types/licensing';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Button } from '../components/ui/Button';
import { FileText } from 'lucide-react';

export const LicensingDashboard = () => {
  const [agreements, setAgreements] = useState<LicenseAgreement[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchAgreements = async () => {
    setLoading(true);
    try {
      const data = await licensingService.getAgreements();
      setAgreements(data.results || []);
    } catch (err: any) {
      setError(err.response?.data?.details || 'Failed to load license agreements');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAgreements();
  }, []);

  return (
    <div className="space-y-8 max-w-7xl mx-auto">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <FileText className="w-8 h-8 text-[#0052D4]" /> Licensing Agreements
        </h1>
        <Button variant="primary" onClick={fetchAgreements}>Refresh</Button>
      </div>

      {error && <div className="p-4 bg-red-50 text-red-700 border border-red-200 rounded-xl">{error}</div>}

      <div className="bg-white shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] rounded-[18px] border border-slate-200 overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow>
              <TableCell isHeader>Agreement ID</TableCell>
              <TableCell isHeader>Request Ref</TableCell>
              <TableCell isHeader>Status</TableCell>
              <TableCell isHeader>Effective Date</TableCell>
              <TableCell isHeader>Expiration</TableCell>
            </TableRow>
          </TableHeader>
          <tbody>
            {loading ? (
              <TableRow><TableCell colSpan={5} className="text-center py-8">Loading agreements...</TableCell></TableRow>
            ) : agreements.length === 0 ? (
              <TableRow>
                <TableCell colSpan={5} className="text-center py-12 text-slate-500">
                  No active license agreements found. <br/>
                </TableCell>
              </TableRow>
            ) : (
              agreements.map(a => (
                <TableRow key={a.id}>
                  <TableCell className="font-mono text-xs">{a.id.split('-')[0]}</TableCell>
                  <TableCell className="font-mono text-xs">{a.request}</TableCell>
                  <TableCell>
                    <span className="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-md uppercase">
                      {a.status.replace('_', ' ')}
                    </span>
                  </TableCell>
                  <TableCell>{a.effective_date ? new Date(a.effective_date).toLocaleDateString() : 'Pending'}</TableCell>
                  <TableCell>{a.expiration_date ? new Date(a.expiration_date).toLocaleDateString() : 'N/A'}</TableCell>
                </TableRow>
              ))
            )}
          </tbody>
        </Table>
      </div>
    </div>
  );
};
