import React from 'react';
import { cn } from '../../utils';

export const Card: React.FC<React.HTMLAttributes<HTMLDivElement> & { gradientTop?: boolean }> = ({ className, gradientTop, ...props }) => {
  return (
    <div 
      className={cn(
        "bg-white border border-slate-200 rounded-[18px] relative overflow-hidden transition-all duration-350 shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] hover:-translate-y-1 hover:border-[#00D2FF]/40 hover:shadow-[0_18px_40px_-5px_rgba(0,210,255,0.2)]",
        gradientTop && "stat-card-gradient",
        className
      )} 
      {...props} 
    />
  );
};

export const CardHeader: React.FC<React.HTMLAttributes<HTMLDivElement>> = ({ className, ...props }) => {
  return <div className={cn("px-6 py-5 font-bold text-[11px] uppercase tracking-[1px] text-slate-500", className)} {...props} />;
};

export const CardContent: React.FC<React.HTMLAttributes<HTMLDivElement>> = ({ className, ...props }) => {
  return <div className={cn("px-6 pb-6 pt-0", className)} {...props} />;
};
