import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { repositoryService } from '../services/repositoryService';
import type { RepositoryConnection } from '../types/repository';
import { Button } from '../components/ui/Button';
import { LoadingState } from '../components/ui/LoadingState';
import { Table, TableHeader, TableRow, TableCell } from '../components/ui/Table';
import { Badge } from '../components/ui/Badge';

export const RepositoryList: React.FC = () => {
  const [repos, setRepos] = useState<RepositoryConnection[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    repositoryService.getConnections().then(data => {
      setRepos(data.results || data as any);
    }).finally(() => setLoading(false));
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Repositories</h1>
        <Link to="/repositories/connect">
          <Button>Connect Repository</Button>
        </Link>
      </div>

      {loading ? <LoadingState /> : (
        <div className="bg-white shadow rounded">
          <Table>
            <TableHeader>
              <TableRow>
                <TableCell isHeader>Repository</TableCell>
                <TableCell isHeader>Provider</TableCell>
                <TableCell isHeader>Status</TableCell>
                <TableCell isHeader>Actions</TableCell>
              </TableRow>
            </TableHeader>
            <tbody>
              {repos.map(r => (
                <TableRow key={r.id}>
                  <TableCell>
                    <div className="font-medium">{r.repo_url}</div>
                    <div className="text-sm text-gray-500">{r.default_branch}</div>
                  </TableCell>
                  <TableCell className="capitalize">{r.provider}</TableCell>
                  <TableCell>
                    <Badge variant={r.status === 'synced' ? 'success' : r.status === 'failed' ? 'danger' : 'warning'}>
                      {r.status}
                    </Badge>
                  </TableCell>
                  <TableCell>
                    <Link to={`/repositories/${r.id}`} className="text-blue-600 hover:underline">Manage</Link>
                  </TableCell>
                </TableRow>
              ))}
              {repos.length === 0 && (
                <TableRow>
                  <TableCell colSpan={4}><div className="py-6 text-center text-gray-500">No repositories connected.</div></TableCell>
                </TableRow>
              )}
            </tbody>
          </Table>
        </div>
      )}
    </div>
  );
};
