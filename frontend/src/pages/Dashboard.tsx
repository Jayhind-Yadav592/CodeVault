import React, { useEffect, useState } from 'react';
import { projectService } from '../services/projectService';
import { DashboardData } from '../types/project';
import { Card, CardContent, CardHeader } from '../components/ui/Card';
import { LoadingState } from '../components/ui/LoadingState';

export const Dashboard: React.FC = () => {
  const [data, setData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const stats = await projectService.getDashboardStats();
        setData(stats);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <LoadingState />;
  if (!data) return <div>Error loading dashboard</div>;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card>
          <CardHeader>Projects</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">{data.projects.total}</div>
            <div className="text-sm text-gray-500">Active: {data.projects.active} | Approved: {data.projects.approved}</div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>Repositories</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">{data.repositories.connected}</div>
            <div className="text-sm text-gray-500">Pending: {data.repositories.pending}</div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>Security Findings</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-red-600">{data.security.open}</div>
            <div className="text-sm text-gray-500">Critical: {data.security.critical} | High: {data.security.high}</div>
          </CardContent>
        </Card>
        
        <Card>
          <CardHeader>Compliance</CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-green-600">{data.compliance.passing}</div>
            <div className="text-sm text-gray-500">Failed: {data.compliance.failed}</div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>Recent Activity</CardHeader>
        <CardContent>
          <ul className="space-y-2">
            {data.recent_activity.map((act, i) => (
              <li key={i} className="text-sm pb-2 border-b last:border-0">
                <span className="font-medium capitalize">{act.action}</span> on {act.resource} 
                <span className="text-gray-400 ml-2">{new Date(act.timestamp).toLocaleString()}</span>
              </li>
            ))}
            {data.recent_activity.length === 0 && <li className="text-gray-500">No recent activity.</li>}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
};
