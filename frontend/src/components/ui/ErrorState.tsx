import React from 'react';

export const ErrorState: React.FC<{ error?: string }> = ({ error = 'An unexpected error occurred.' }) => (
  <div className="flex flex-col items-center justify-center p-12 text-center">
    <div className="text-red-500 mb-4 text-4xl">!</div>
    <h3 className="text-lg font-medium text-gray-900 mb-2">Something went wrong</h3>
    <p className="text-gray-500">{error}</p>
  </div>
);
