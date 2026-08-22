import React from 'react';
import { cn } from '../../utils';

export const Table: React.FC<React.TableHTMLAttributes<HTMLTableElement>> = ({ className, ...props }) => {
  return (
    <div className="w-full overflow-auto rounded-[18px] border border-slate-200 shadow-sm bg-white">
      <table className={cn("w-full caption-bottom text-sm border-collapse", className)} {...props} />
    </div>
  );
};

export const TableHeader: React.FC<React.HTMLAttributes<HTMLTableSectionElement>> = ({ className, ...props }) => {
  return <thead className={cn("[&_tr]:border-b border-slate-200 bg-slate-50/50", className)} {...props} />;
};

export const TableRow: React.FC<React.HTMLAttributes<HTMLTableRowElement>> = ({ className, ...props }) => {
  return (
    <tr 
      className={cn("border-b border-slate-200 transition-colors hover:bg-slate-50/80 data-[state=selected]:bg-slate-50", className)} 
      {...props} 
    />
  );
};

export const TableCell: React.FC<React.TdHTMLAttributes<HTMLTableCellElement> & { isHeader?: boolean }> = ({ 
  className, 
  isHeader, 
  ...props 
}) => {
  const Component = isHeader ? 'th' : 'td';
  return (
    <Component 
      className={cn(
        "p-4 align-middle [&:has([role=checkbox])]:pr-0",
        isHeader 
          ? "h-12 px-4 text-left align-middle font-semibold text-slate-500 text-[12px] uppercase tracking-wider" 
          : "text-[13px] text-slate-700 font-medium",
        className
      )} 
      {...props} 
    />
  );
};
