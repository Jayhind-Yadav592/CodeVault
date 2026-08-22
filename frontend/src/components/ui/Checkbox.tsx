import React from 'react';
import { cn } from '../../utils';

export interface CheckboxProps extends React.HTMLAttributes<HTMLDivElement> {
    variant?: 'primary' | 'secondary' | 'danger' | 'success';
    disabled?: boolean;
}

export const Checkbox: React.FC<CheckboxProps> = ({ children, className, variant = 'primary', disabled, ...props }) => {
    return (
        <div className={cn('base-style', variant, disabled && 'opacity-100', className)} {...props}>
            {children}
        </div>
    );
};
