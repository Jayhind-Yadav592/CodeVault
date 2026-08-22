export interface MarketplaceListing {
  id: string;
  project: {
    id: string;
    name: string;
    description: string;
  } | string;
  visibility: 'private' | 'unlisted' | 'public';
  status: 'draft' | 'pending_publication' | 'published' | 'paused' | 'unpublished' | 'archived';
  popularity_score: number;
  views_count: number;
  saves_count: number;
  created_at?: string;
}
