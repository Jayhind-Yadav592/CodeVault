import React from 'react';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { repositoryService } from '../services/repositoryService';
import type { RepositoryConnection, AnalysisSnapshot, TrainPlexReadiness } from '../types/repository';
import { LoadingState } from '../components/ui/LoadingState';
import { Badge } from '../components/ui/Badge';
import { Card, CardHeader, CardContent } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Alert } from '../components/ui/Alert';

export const RepositoryDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [repo, setRepo] = useState<RepositoryConnection | null>(null);
  const [snapshot, setSnapshot] = useState<AnalysisSnapshot | null>(null);
  const [readiness, setReadiness] = useState<TrainPlexReadiness | null>(null);
  const [loading, setLoading] = useState(true);
  const [syncing, setSyncing] = useState(false);
  const [tab, setTab] = useState('overview');

  const fetchData = React.useCallback(async () => {
    if (!id) return;
    try {
      const r = await repositoryService.getConnection(id);
      setRepo(r);
      if (r.status === 'synced') {
        const snap = await repositoryService.getLatestSnapshot(id).catch(() => null);
        setSnapshot(snap);
        const ready = await repositoryService.getTrainPlexReadiness(id).catch(() => null);
        setReadiness(ready);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }, [id]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleSync = async () => {
    if (!id) return;
    setSyncing(true);
    try {
      await repositoryService.syncRepository(id);
      alert('Analysis triggered! Refresh in a few minutes.');
      fetchData();
    } catch (e) {
      alert('Failed to trigger analysis');
    } finally {
      setSyncing(false);
    }
  };

  if (loading) return <LoadingState />;
  if (!repo) return <div>Repository not found</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center border-b pb-4">
        <div>
          <h1 className="text-3xl font-bold mb-1">{repo.repo_name || repo.repo_url}</h1>
          <Badge>{repo.status}</Badge>
        </div>
        <Button onClick={handleSync} isLoading={syncing}>Analyze Repository</Button>
      </div>

      <div className="flex gap-4 border-b overflow-x-auto">
        <button onClick={() => setTab('overview')} className={`px-4 py-2 ${tab === 'overview' ? 'border-b-2 border-blue-600 font-medium text-blue-600' : 'text-gray-900'}`}>Overview & Git</button>
        <button onClick={() => setTab('readiness')} className={`px-4 py-2 ${tab === 'readiness' ? 'border-b-2 border-blue-600 font-medium text-blue-600' : 'text-gray-900'}`}>TrainPlex Readiness</button>
      </div>

      {tab === 'overview' && (
        <div className="grid grid-cols-2 gap-6">
          <Card>
            <CardHeader>Repository Information</CardHeader>
            <CardContent className="space-y-2">
              <div className="flex justify-between"><span>Provider:</span> <span className="capitalize">{repo.provider}</span></div>
              <div className="flex justify-between"><span>Branch:</span> <span>{repo.default_branch}</span></div>
              <div className="flex justify-between"><span>URL:</span> <a href={repo.repo_url} target="_blank" rel="noreferrer" className="text-blue-500 hover:underline">Link</a></div>
            </CardContent>
          </Card>
          
          {snapshot ? (
            <Card>
              <CardHeader>Git & Code Metrics</CardHeader>
              <CardContent className="space-y-2">
                <div className="flex justify-between"><span>Total LOC:</span> <span>{snapshot.total_loc?.toLocaleString() || 0}</span></div>
                <div className="flex justify-between font-medium"><span>Meaningful LOC:</span> <span>{snapshot.meaningful_loc?.toLocaleString() || 0}</span></div>
                <div className="flex justify-between"><span>Commits:</span> <span>{snapshot.meaningful_commits?.toLocaleString() || 0}</span></div>
                <div className="flex justify-between"><span>Files:</span> <span>{snapshot.total_files?.toLocaleString() || 0}</span></div>
              </CardContent>
            </Card>
          ) : (
            <Card><CardContent className="pt-6"><Alert type="warning">No analysis data available. Please analyze the repository.</Alert></CardContent></Card>
          )}
        </div>
      )}

      {tab === 'readiness' && readiness && (
        <div className="space-y-6">
          <h2 className="text-xl font-bold">TrainPlex Readiness Evaluation</h2>
          <div className="grid grid-cols-2 gap-4">
            <Card>
              <CardHeader>Volume Requirements</CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Minimum 50,000 LOC</span>
                  <div className="flex items-center gap-2">
                    <span className="text-sm text-gray-900">Actual: {readiness.size.value}</span>
                    <Badge variant={readiness.size.status === 'PASS' ? 'success' : 'danger'}>{readiness.size.status}</Badge>
                  </div>
                </div>
                <div className="flex justify-between items-center border-b pb-2">
                  <span>5+ Meaningful Commits</span>
                  <div className="flex items-center gap-2">
                    <span className="text-sm text-gray-900">Actual: {readiness.commits.value}</span>
                    <Badge variant={readiness.commits.status === 'PASS' ? 'success' : 'danger'}>{readiness.commits.status}</Badge>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>Legal & Security</CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Creator Ownership</span>
                  <Badge variant={readiness.ownership.declaration === 'PASS' ? 'success' : 'warning'}>{readiness.ownership.declaration}</Badge>
                </div>
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Open Source Contamination</span>
                  <Badge variant="warning">{readiness.ownership.opensource_contamination}</Badge>
                </div>
                <div className="flex justify-between items-center border-b pb-2">
                  <span>Secret Exposure</span>
                  <Badge variant="success">{readiness.security.secrets}</Badge>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      )}
      {tab === 'readiness' && !readiness && (
        <Alert type="error">Readiness data requires a completed repository analysis.</Alert>
      )}
    </div>
  );
};
