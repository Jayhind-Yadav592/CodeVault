import React, { forwardRef } from 'react';
import { cn } from '../../utils';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  isLoading?: boolean;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'primary', isLoading, children, ...props }, ref) => {
    const baseStyles = 'inline-flex items-center justify-center gap-2 px-6 py-2.5 font-sans text-sm font-bold border-none rounded-xl cursor-pointer transition-all duration-350 whitespace-nowrap relative overflow-hidden focus:outline-none';
    
    const variants = {
      primary: 'bg-gradient-to-br from-[#0052D4] to-[#00D2FF] text-white shadow-[0_4px_20px_rgba(0,210,255,0.35)] hover:-translate-y-0.5 hover:shadow-[0_6px_25px_rgba(0,210,255,0.45)]',
      secondary: 'bg-white text-slate-700 border border-slate-200 shadow-sm hover:border-[#00D2FF] hover:text-[#0052D4] hover:shadow-[0_4px_15px_rgba(0,210,255,0.1)]',
      danger: 'bg-gradient-to-br from-red-500 to-red-400 text-white shadow-[0_4px_20px_rgba(239,68,68,0.35)] hover:-translate-y-0.5',
      ghost: 'bg-transparent text-slate-600 hover:bg-slate-100 hover:text-slate-900',
    };

    return (
      <button
        ref={ref}
        className={cn(baseStyles, variants[variant], className, isLoading && 'opacity-80 cursor-not-allowed')}
        {...props}
      >
        {isLoading ? 'Loading...' : children}
      </button>
    );
  }
);
Button.displayName = 'Button';
