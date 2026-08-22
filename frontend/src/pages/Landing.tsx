import React from 'react';
import { Link } from 'react-router-dom';
import { Shield, ArrowRight, Lock, Code, Activity } from 'lucide-react';
import { Button } from '../components/ui/Button';

export const Landing: React.FC = () => {
  return (
    <div className="min-h-screen relative font-sans text-slate-900 overflow-hidden">
      {/* Background Canvas from Lionlx */}
      <div className="bg-canvas">
        <div className="orb orb1"></div>
        <div className="orb orb2"></div>
        <div className="orb orb3"></div>
      </div>

      {/* Navigation */}
      <nav className="relative z-10 flex items-center justify-between px-8 py-6 max-w-7xl mx-auto">
        <div className="flex items-center gap-3 font-bold text-2xl text-slate-900">
          <Shield className="w-8 h-8 text-[#0052D4]" />
          CodeVault
        </div>
        <div className="flex items-center gap-4">
          <Link to="/login" className="text-slate-600 font-medium hover:text-[#0052D4] transition-colors">Sign In</Link>
          <Link to="/login">
            <Button variant="primary">Get Started</Button>
          </Link>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="relative z-10 flex flex-col items-center text-center pt-32 px-4 max-w-5xl mx-auto">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50/80 border border-blue-200/50 text-[#0052D4] font-semibold text-sm mb-8 shadow-sm backdrop-blur-sm">
          <span className="w-2 h-2 rounded-full bg-[#00D2FF] animate-pulse"></span>
          TrainPlex Enterprise Platform 2.0
        </div>
        
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-8 leading-tight">
          Secure, Analyze, and <br/>
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#0052D4] to-[#00D2FF]">
            License Your Software
          </span>
        </h1>
        
        <p className="text-lg md:text-xl text-slate-600 max-w-3xl mb-12 leading-relaxed">
          The proprietary repository management platform built for TrainPlex. Automate technical analysis, run continuous compliance rules, manage security reviews, and distribute intellectual property globally.
        </p>

        <div className="flex items-center gap-4 flex-col sm:flex-row">
          <Link to="/login">
            <Button variant="primary" className="!px-8 !py-4 text-base">
              Enter Dashboard <ArrowRight className="w-5 h-5 ml-1" />
            </Button>
          </Link>
          <a href="#features" className="px-8 py-4 text-base font-semibold text-slate-700 bg-white border border-slate-200 rounded-xl hover:border-[#00D2FF] hover:text-[#0052D4] hover:shadow-[0_4px_15px_rgba(0,210,255,0.1)] transition-all">
            Learn More
          </a>
        </div>

        {/* Feature Highlights */}
        <div className="grid md:grid-cols-3 gap-8 mt-32 w-full text-left">
          <div className="bg-white/80 backdrop-blur-md p-8 rounded-2xl border border-slate-200 shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] hover:-translate-y-1 transition-transform relative overflow-hidden stat-card-gradient">
            <Lock className="w-10 h-10 text-[#0052D4] mb-4" />
            <h3 className="text-xl font-bold mb-3">Enterprise Security</h3>
            <p className="text-slate-600">Continuous vulnerability scanning, SAST/DAST analysis, and dependency auditing before your code is licensed.</p>
          </div>
          <div className="bg-white/80 backdrop-blur-md p-8 rounded-2xl border border-slate-200 shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] hover:-translate-y-1 transition-transform relative overflow-hidden stat-card-gradient">
            <Code className="w-10 h-10 text-[#00D2FF] mb-4" />
            <h3 className="text-xl font-bold mb-3">Repository Analytics</h3>
            <p className="text-slate-600">Deep structural analysis of Git repositories. Track LOC, PR velocity, author contributions, and maintainability.</p>
          </div>
          <div className="bg-white/80 backdrop-blur-md p-8 rounded-2xl border border-slate-200 shadow-[0_10px_30px_-5px_rgba(0,82,212,0.05)] hover:-translate-y-1 transition-transform relative overflow-hidden stat-card-gradient">
            <Activity className="w-10 h-10 text-[#00F0FF] mb-4" />
            <h3 className="text-xl font-bold mb-3">TrainPlex Compliance</h3>
            <p className="text-slate-600">Automated legal and architectural rule engines verifying intellectual property ownership and enterprise standards.</p>
          </div>
        </div>
      </main>
    </div>
  );
};
