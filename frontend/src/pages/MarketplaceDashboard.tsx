import { useEffect, useState } from 'react';
import { marketplaceService } from '../services/marketplaceService';
import type { MarketplaceListing } from '../types/marketplace';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Button } from '../components/ui/Button';
import { ShoppingBag } from 'lucide-react';

export const MarketplaceDashboard = () => {
  const [listings, setListings] = useState<MarketplaceListing[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchListings = async () => {
    setLoading(true);
    try {
      const data = await marketplaceService.getListings();
      setListings(data.results || []);
    } catch (err: any) {
      setError(err.response?.data?.details || 'Failed to load marketplace listings');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchListings();
  }, []);

  return (
    <div className="space-y-8 max-w-7xl mx-auto">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <ShoppingBag className="w-8 h-8 text-[#0052D4]" /> Marketplace
        </h1>
        <Button variant="primary" onClick={fetchListings}>Refresh Listings</Button>
      </div>

      {error && <div className="p-4 bg-red-50 text-red-700 border border-red-200 rounded-xl">{error}</div>}

      <div className="bg-white shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] rounded-[18px] border border-slate-200 overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow>
              <TableCell isHeader>Project</TableCell>
              <TableCell isHeader>Visibility</TableCell>
              <TableCell isHeader>Status</TableCell>
              <TableCell isHeader>Views</TableCell>
              <TableCell isHeader>Score</TableCell>
            </TableRow>
          </TableHeader>
          <tbody>
            {loading ? (
              <TableRow><TableCell colSpan={5} className="text-center py-8">Loading marketplace catalog...</TableCell></TableRow>
            ) : listings.length === 0 ? (
              <TableRow>
                <TableCell colSpan={5} className="text-center py-12 text-slate-500">
                  No marketplace listings currently available.
                </TableCell>
              </TableRow>
            ) : (
              listings.map(l => (
                <TableRow key={l.id}>
                  <TableCell className="font-semibold text-[#0052D4]">
                    {typeof l.project === 'object' ? l.project.name : l.project}
                  </TableCell>
                  <TableCell className="capitalize">{l.visibility}</TableCell>
                  <TableCell>
                    <span className="px-2 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded-md uppercase">
                      {l.status.replace('_', ' ')}
                    </span>
                  </TableCell>
                  <TableCell>{l.views_count}</TableCell>
                  <TableCell>{l.popularity_score}</TableCell>
                </TableRow>
              ))
            )}
          </tbody>
        </Table>
      </div>
    </div>
  );
};
