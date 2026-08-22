import React from 'react';

export const Table = ({ children }: { children: React.ReactNode }) => (
  <div className="overflow-x-auto w-full">
    <table className="w-full text-sm text-left">{children}</table>
  </div>
);

export const TableHeader = ({ children }: { children: React.ReactNode }) => (
  <thead className="text-xs text-gray-700 uppercase bg-gray-50 border-b">{children}</thead>
);

export const TableRow = ({ children }: { children: React.ReactNode }) => (
  <tr className="bg-white border-b hover:bg-gray-50">{children}</tr>
);

export const TableCell = ({ children, isHeader = false }: { children: React.ReactNode; isHeader?: boolean }) => {
  if (isHeader) return <th className="px-6 py-3">{children}</th>;
  return <td className="px-6 py-4">{children}</td>;
};
