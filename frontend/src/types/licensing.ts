export interface LicenseAgreement {
  id: string;
  status: 'draft' | 'pending_signature' | 'partially_signed' | 'fully_signed' | 'active' | 'expired' | 'terminated';
  effective_date: string | null;
  expiration_date: string | null;
  request: string;
  created_at: string;
}

export interface LicenseRequest {
  id: string;
  status: 'draft' | 'submitted' | 'under_review' | 'negotiation' | 'terms_agreed' | 'agreement_pending' | 'signed' | 'active' | 'rejected' | 'cancelled' | 'expired' | 'terminated';
  product: string;
  organization: string;
  intended_usage: string;
  created_at: string;
}
