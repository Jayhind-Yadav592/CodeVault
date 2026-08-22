export interface FinanceTransaction {
  id: string;
  transaction_type: 'payment' | 'payout' | 'refund' | 'adjustment' | 'fee';
  status: 'pending' | 'completed' | 'failed' | 'reversed';
  currency: string;
  description: string;
  project?: string;
  agreement?: string;
  created_at: string;
}
