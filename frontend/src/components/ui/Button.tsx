import React, { forwardRef } from 'react';
import { cn } from '../../utils';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger';
  isLoading?: boolean;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'primary', isLoading, children, ...props }, ref) => {
    const baseStyles = 'px-4 py-2 rounded font-medium focus:outline-none transition-colors';
    const variants = {
      primary: 'bg-blue-600 text-white hover:bg-blue-700',
      secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
      danger: 'bg-red-600 text-white hover:bg-red-700',
    };

    return (
      <button
        ref={ref}
        className={cn(baseStyles, variants[variant], className, isLoading && 'opacity-50 cursor-not-allowed')}
        disabled={isLoading || props.disabled}
        {...props}
      >
        {isLoading ? 'Loading...' : children}
      </button>
    );
  }
);
Button.displayName = 'Button';
