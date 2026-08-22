import os
import re
from typing import List, Dict, Any
from .models import Finding, Dependency

class ScannerContext:
    def __init__(self, project, snapshot, repo_path):
        self.project = project
        self.snapshot = snapshot
        self.repo_path = repo_path

class BaseScanner:
    scanner_id = None
    name = None
    description = None

    def scan(self, context: ScannerContext) -> List[Finding]:
        raise NotImplementedError
        
    def _create_finding(self, context, category, severity, confidence, file_path, line_number, rule_id, desc, evidence, remediation):
        return Finding(
            project=context.project,
            snapshot=context.snapshot,
            scanner_id=self.scanner_id,
            category=category,
            severity=severity,
            confidence=confidence,
            file_path=file_path,
            line_number=line_number,
            rule_identifier=rule_id,
            short_description=desc,
            redacted_evidence=evidence,
            remediation=remediation
        )

# ================================
# Secrets & Credentials
# ================================
class SecretScanner(BaseScanner):
    scanner_id = 'core.secret_scanner'
    name = 'Secret and Credential Scanner'
    description = 'Detects hardcoded secrets, tokens, and credentials.'

    def scan(self, context: ScannerContext) -> List[Finding]:
        findings = []
        patterns = {
            'aws_key': (r'AKIA[0-9A-Z]{16}', 'AWS Access Key'),
            'generic_secret': (r'(?i)(password|secret|token|api_key)\s*[:=]\s*["\']([a-zA-Z0-9_\-]{16,})["\']', 'Generic Secret'),
            'private_key': (r'-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----', 'Private Key'),
            'jwt': (r'eyJ[a-zA-Z0-9_-]+\.eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+', 'JWT Token')
        }
        
        for root, _, files in os.walk(context.repo_path):
            if '.git' in root: continue
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, context.repo_path)
                
                # Skip large/binary files
                if os.path.getsize(filepath) > 1024 * 1024: continue
                
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for i, line in enumerate(f):
                            for key, (pat, name) in patterns.items():
                                match = re.search(pat, line)
                                if match:
                                    # REDACT EVIDENCE
                                    redacted = line.strip()
                                    if key == 'generic_secret' and len(match.groups()) > 1:
                                        redacted = redacted.replace(match.group(2), '[REDACTED]')
                                    elif key in ['aws_key', 'jwt']:
                                        redacted = '[REDACTED]'
                                    else:
                                        redacted = '[REDACTED SECRET MATERIAL]'
                                        
                                    findings.append(self._create_finding(
                                        context, Finding.Category.SECRET, Finding.Severity.CRITICAL, 'HIGH',
                                        rel_path, i + 1, key, f'Found potential {name}',
                                        redacted, 'Remove secret from repository, revoke it, and inject via environment variables.'
                                    ))
                except Exception:
                    pass
        return findings

class SensitiveFileScanner(BaseScanner):
    scanner_id = 'core.sensitive_file_scanner'
    name = 'Sensitive File Scanner'
    description = 'Detects files that typically contain sensitive configurations.'

    def scan(self, context: ScannerContext) -> List[Finding]:
        findings = []
        sensitive_patterns = [r'\.env$', r'\.env\..*', r'credentials\.json', r'secrets\.yml', r'.*\.pem$', r'.*\.key$', r'id_rsa$']
        
        for root, _, files in os.walk(context.repo_path):
            if '.git' in root: continue
            for file in files:
                for pat in sensitive_patterns:
                    if re.match(pat, file):
                        filepath = os.path.join(root, file)
                        rel_path = os.path.relpath(filepath, context.repo_path)
                        findings.append(self._create_finding(
                            context, Finding.Category.CONFIGURATION, Finding.Severity.HIGH, 'HIGH',
                            rel_path, None, 'sensitive_file', f'Sensitive file pattern matched: {file}',
                            f'File path: {rel_path}', 'Ensure this file does not contain real production credentials.'
                        ))
        return findings

# ================================
# PII
# ================================
class PIIScanner(BaseScanner):
    scanner_id = 'core.pii_scanner'
    name = 'PII Scanner'
    description = 'Detects Personally Identifiable Information.'

    def scan(self, context: ScannerContext) -> List[Finding]:
        findings = []
        patterns = {
            'email': (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'Email Address'),
            'ssn': (r'\b\d{3}-\d{2}-\d{4}\b', 'SSN-like pattern')
        }
        
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root or 'test' in root.lower() or 'vendor' in root.lower() or 'node_modules' in root.lower(): continue
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, context.repo_path)
                if os.path.getsize(filepath) > 1024 * 512: continue
                
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for i, line in enumerate(f):
                            for key, (pat, name) in patterns.items():
                                match = re.search(pat, line)
                                if match:
                                    val = match.group(0)
                                    # Exclude common test/demo emails
                                    if 'example.com' in val or 'test' in val or 'demo' in val:
                                        continue
                                        
                                    findings.append(self._create_finding(
                                        context, Finding.Category.PII, Finding.Severity.MEDIUM, 'MEDIUM',
                                        rel_path, i + 1, key, f'Found potential {name}',
                                        '[REDACTED PII]', 'Ensure real PII is not hardcoded. Use synthetic data for tests.'
                                    ))
                except Exception:
                    pass
        return findings

# ================================
# Licenses & Ownership
# ================================
class LicenseScanner(BaseScanner):
    scanner_id = 'core.license_scanner'
    name = 'License Scanner'
    description = 'Detects open-source licenses in repository.'

    def scan(self, context: ScannerContext) -> List[Finding]:
        findings = []
        forbidden_licenses = {
            'gpl': 'GPL (General Public License)',
            'agpl': 'AGPL (Affero General Public License)'
        }
        
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root: continue
            
            # Determine context
            is_vendor = 'vendor' in root.lower() or 'node_modules' in root.lower()
            
            for file in files:
                lower = file.lower()
                if 'license' in lower or 'copying' in lower:
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, context.repo_path)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read().lower()
                            for key, name in forbidden_licenses.items():
                                if key in content or 'gnu general public license' in content or 'affero general public license' in content:
                                    if 'affero' in content: key, name = 'agpl', forbidden_licenses['agpl']
                                    elif 'gnu' in content: key, name = 'gpl', forbidden_licenses['gpl']
                                    
                                    cat = Finding.Category.THIRD_PARTY if is_vendor else Finding.Category.LICENSE
                                    severity = Finding.Severity.CRITICAL if not is_vendor else Finding.Severity.HIGH
                                    findings.append(self._create_finding(
                                        context, cat, severity, 'HIGH',
                                        rel_path, None, f'prohibited_license_{key}', f'Prohibited license found: {name}',
                                        f'Found {name} text in {rel_path}', 'Remove the reciprocally-licensed open source code.'
                                    ))
                                    break
                    except:
                        pass
        return findings

class CopyrightScanner(BaseScanner):
    scanner_id = 'core.copyright_scanner'
    name = 'Copyright and Ownership Scanner'
    description = 'Detects third-party copyright headers and proprietary markers.'

    def scan(self, context: ScannerContext) -> List[Finding]:
        findings = []
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root or 'vendor' in root.lower() or 'node_modules' in root.lower(): continue
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, context.repo_path)
                if os.path.getsize(filepath) > 1024 * 512: continue
                
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for i, line in enumerate(f):
                            if i > 50: break # Usually at the top
                            lower = line.lower()
                            if 'copyright' in lower or 'proprietary' in lower or 'confidential' in lower:
                                # We flag it for human review if it's found in project source
                                findings.append(self._create_finding(
                                    context, Finding.Category.OWNERSHIP, Finding.Severity.MEDIUM, 'LOW',
                                    rel_path, i + 1, 'copyright_header', 'Potential third-party copyright or confidential marker.',
                                    line.strip()[:100], 'Verify if this marker belongs to a third-party or the author.'
                                ))
                except:
                    pass
        return findings

# ================================
# Dependencies
# ================================
class DependencyScanner(BaseScanner):
    scanner_id = 'core.dependency_scanner'
    name = 'Dependency Scanner'
    description = 'Extracts dependency metadata.'

    def scan(self, context: ScannerContext) -> List[Finding]:
        # This scanner actually populates the Dependency model, not just Findings.
        # But for architecture simplicity, it can do both or just populate Dependencies.
        manifests = {
            'requirements.txt': Dependency.Ecosystem.PYTHON,
            'package.json': Dependency.Ecosystem.NPM,
            'pom.xml': Dependency.Ecosystem.JAVA,
            'go.mod': Dependency.Ecosystem.GO,
            'Cargo.toml': Dependency.Ecosystem.RUST,
            'composer.json': Dependency.Ecosystem.PHP,
            'Gemfile': Dependency.Ecosystem.RUBY,
        }
        
        for root, dirs, files in os.walk(context.repo_path):
            if '.git' in root or 'vendor' in root.lower() or 'node_modules' in root.lower(): continue
            for file in files:
                if file in manifests:
                    ecosystem = manifests[file]
                    rel_path = os.path.relpath(os.path.join(root, file), context.repo_path)
                    
                    # Create a Dependency record (simplified extraction)
                    Dependency.objects.create(
                        project=context.project,
                        snapshot=context.snapshot,
                        name=f'Manifest: {rel_path}',
                        ecosystem=ecosystem,
                        manifest_source=rel_path
                    )
                    
        return [] # Returns no explicitly bad findings, just populates DB.
