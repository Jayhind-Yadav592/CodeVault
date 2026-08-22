import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

BASE = r"c:\Users\admin\Documents\TrainPlex\CodeVault\frontend\src\components\ui"

COMPONENTS = {
    "Input.tsx": """
import React from 'react';
import { cn } from '../../utils';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

export const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, ...props }, ref) => {
    return (
      <div className="w-full">
        {label && <label className="block text-sm font-medium text-gray-700 mb-1">{label}</label>}
        <input
          ref={ref}
          className={cn(
            'w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
            error && 'border-red-500 focus:ring-red-500',
            className
          )}
          {...props}
        />
        {error && <span className="text-sm text-red-500 mt-1 block">{error}</span>}
      </div>
    );
  }
);
Input.displayName = 'Input';
""",
    "Card.tsx": """
import React from 'react';
import { cn } from '../../utils';

export const Card = ({ className, children }: { className?: string; children: React.ReactNode }) => (
  <div className={cn("bg-white rounded-lg border border-gray-200 shadow-sm", className)}>
    {children}
  </div>
);

export const CardHeader = ({ className, children }: { className?: string; children: React.ReactNode }) => (
  <div className={cn("px-6 py-4 border-b border-gray-200", className)}>{children}</div>
);

export const CardContent = ({ className, children }: { className?: string; children: React.ReactNode }) => (
  <div className={cn("p-6", className)}>{children}</div>
);
""",
    "Badge.tsx": """
import React from 'react';
import { cn } from '../../utils';

interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  variant?: 'default' | 'success' | 'warning' | 'danger';
}

export const Badge: React.FC<BadgeProps> = ({ variant = 'default', className, children, ...props }) => {
  const variants = {
    default: 'bg-gray-100 text-gray-800',
    success: 'bg-green-100 text-green-800',
    warning: 'bg-yellow-100 text-yellow-800',
    danger: 'bg-red-100 text-red-800',
  };

  return (
    <span className={cn('px-2.5 py-0.5 rounded-full text-xs font-medium', variants[variant], className)} {...props}>
      {children}
    </span>
  );
};
""",
    "Alert.tsx": """
import React from 'react';
import { cn } from '../../utils';

interface AlertProps {
  type?: 'info' | 'success' | 'warning' | 'error';
  title?: string;
  children: React.ReactNode;
}

export const Alert: React.FC<AlertProps> = ({ type = 'info', title, children }) => {
  const styles = {
    info: 'bg-blue-50 text-blue-800 border-blue-200',
    success: 'bg-green-50 text-green-800 border-green-200',
    warning: 'bg-yellow-50 text-yellow-800 border-yellow-200',
    error: 'bg-red-50 text-red-800 border-red-200',
  };

  return (
    <div className={cn('p-4 border rounded-md', styles[type])}>
      {title && <h4 className="font-semibold mb-1">{title}</h4>}
      <div className="text-sm">{children}</div>
    </div>
  );
};
""",
    "LoadingState.tsx": """
import React from 'react';

export const LoadingState: React.FC<{ message?: string }> = ({ message = 'Loading...' }) => (
  <div className="flex flex-col items-center justify-center p-8 text-gray-500">
    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500 mb-4"></div>
    <p>{message}</p>
  </div>
);
""",
    "EmptyState.tsx": """
import React from 'react';

export const EmptyState: React.FC<{ title: string; description?: string }> = ({ title, description }) => (
  <div className="flex flex-col items-center justify-center p-12 text-center border-2 border-dashed border-gray-200 rounded-lg bg-gray-50">
    <h3 className="text-lg font-medium text-gray-900 mb-1">{title}</h3>
    {description && <p className="text-gray-500 max-w-sm">{description}</p>}
  </div>
);
""",
    "ErrorState.tsx": """
import React from 'react';

export const ErrorState: React.FC<{ error?: string }> = ({ error = 'An unexpected error occurred.' }) => (
  <div className="flex flex-col items-center justify-center p-12 text-center">
    <div className="text-red-500 mb-4 text-4xl">!</div>
    <h3 className="text-lg font-medium text-gray-900 mb-2">Something went wrong</h3>
    <p className="text-gray-500">{error}</p>
  </div>
);
""",
    "Table.tsx": """
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
""",
}

for name, content in COMPONENTS.items():
    write_file(os.path.join(BASE, name), content)

print("UI components generated successfully!")
