import React from 'react';
import { cn } from '../../utils';

export interface AvatarProps extends React.HTMLAttributes<HTMLDivElement> {
    variant?: 'primary' | 'secondary' | 'danger' | 'success';
    disabled?: boolean;
}

export const Avatar: React.FC<AvatarProps> = ({ children, className, variant = 'primary', disabled, ...props }) => {
    return (
        <div className={cn('base-style', variant, disabled && 'opacity-100', className)} {...props}>
            {children}
        </div>
    );
};
