import React from 'react';
import { cn } from '../../utils';

export interface TimelineProps extends React.HTMLAttributes<HTMLDivElement> {
    variant?: 'primary' | 'secondary' | 'danger' | 'success';
    disabled?: boolean;
}

export const Timeline: React.FC<TimelineProps> = ({ children, className, variant = 'primary', disabled, ...props }) => {
    return (
        <div className={cn('base-style', variant, disabled && 'opacity-50', className)} {...props}>
            {children}
        </div>
    );
};
