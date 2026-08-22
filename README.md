# CodeVault — Phase 1: Production Foundation

CodeVault is a Proprietary Software Licensing & Repository Management Platform designed to fulfill complex enterprise repository requirements.

This repository currently implements the **Phase 1 Production Foundation**, which provides the base architecture, authentication, authorization, and modular structure upon which the full platform will be built.

## Architecture Overview

CodeVault is built on a modern Python stack:
- **Backend Framework**: Django 5.x
- **API Framework**: Django REST Framework (DRF)
- **Database**: PostgreSQL (Production), SQLite (Local Development)
- **Authentication**: JWT (JSON Web Tokens) via SimpleJWT
- **Testing**: pytest + pytest-django

The project uses a highly modular structure to separate concerns.

### Project Structure

```text
codevault/
├── codevault/          # Django project configuration
├── core/               # Abstract base models, unified exceptions, base Web UI
├── accounts/           # Custom User model and authentication APIs
├── audit/              # Audit logging foundation
├── developers/         # Developer profiles and dashboard APIs
├── projects/           # Core Project Management, Categories, and Lifecycle
├── notifications/      # User notifications
├── repositories/       # Git repository management (scaffolded)
├── reviews/            # Code review and PR management (scaffolded)
├── compliance/         # Compliance checks and enforcement (scaffolded)
├── licensing/          # Proprietary licensing management (scaffolded)
├── finance/            # Billing and financial logic (scaffolded)
├── analytics/          # Platform analytics (scaffolded)
```

## Phase 2: Developer & Project Management

Phase 2 introduces a complete Developer and Software Project Management subsystem.
- **Developer Profiles**: Rich profiles with stats and completion tracking.
- **Project Lifecycle Engine**: State machine for transitioning projects from DRAFT -> SUBMITTED -> UNDER_REVIEW.
- **Ownership Declaration**: Versioned, immutable ownership signatures required for project submission.
- **RBAC APIs**: Strict cross-user data isolation via `IsProjectOwner` permissions.
- **Search & Filter**: Powerful querying capabilities via `django-filter` integration.

## Phase 3: Repository Integration & Intelligence Engine

Phase 3 introduces the core engine for scanning, classifying, and extracting metadata from Git repositories.
- **Git Integration Engine**: Safe, full-fidelity interaction with local and remote Git repositories using `GitPython`.
- **Code Classifier & LOC Analyzer**: Fast, heuristic-based categorization of source, binary, documentation, and dependency files. Extracts granular line-of-code statistics (total, code, blank, comments) supporting over 30 languages.
- **Immutable Snapshots**: Generates immutable `AnalysisSnapshot` records for auditable historical comparisons of a project's scale over time.
- **Asynchronous Execution**: Powered natively by `django-q2`, avoiding external broker dependencies like Redis to guarantee clean execution across all environments (including Windows).

## Phase 4: Compliance, Eligibility & Quality Evaluation Engine

Phase 4 introduces a dynamic, modular rule engine that validates repository snapshots against CodeVault/TrainPlex policies.
- **Configurable Policies**: Weighted scoring, threshold management (e.g., 50k LOC, 5 commits).
- **Deep Repository Scanning**: Specialized scanners re-clone snapshots asynchronously to inspect for PII, secrets, prohibited open-source licenses, test coverage, and documentation.
- **Secret Redaction & Security**: Findings are structurally redacted before persistence. The engine guarantees plaintext secrets never touch the database.
- **Transparent Scoring & Decision Matrix**: Rules produce verifiable `RuleResult` evidence, culminating in explicit categorizations (`ELIGIBLE`, `REQUIRES_HUMAN_REVIEW`, etc.) with actionable remediations.
- **API & UI**: Provides detailed requirement matrices via the Compliance Dashboard and DRF APIs.

## Phase 5: Deep Security, License & Intellectual Property Analysis

Phase 5 introduces an advanced security and intellectual property scanning subsystem.
- **Specialized Scanner Framework**: Deploys independent heuristic and regex-based scanners for secrets, PII, dependencies, licensing, and proprietary copyright headers.
- **Strict Evidence Redaction**: Context-aware redaction replaces identified sensitive material (e.g., JWTs, AWS Keys, SSNs) with safe placeholder tags (`[REDACTED]`) before they hit the ORM.
- **Cross-Phase Integration**: Seamlessly integrates into Phase 4, turning security discoveries into critical, automated compliance failures requiring human-review overrides.
- **Reviewer Workflow**: Maintains an immutable `FindingActivity` ledger to audit every finding interaction, including resolving, acknowledging, and marking false positives.

## Phase 6: Multi-Stage Review, Approval & Remediation Workflow

Phase 6 implements the authoritative human-in-the-loop workflow, bridging automated scanner insights with final eligibility determination.
- **Strict State Machine**: Enforces a rigid lifecycle (`TRIAGE` -> `TECHNICAL_REVIEW` -> `IP_REVIEW` -> `SECURITY_REVIEW` -> `COMPLIANCE_REVIEW` -> `FINAL_REVIEW`).
- **Granular RBAC**: Defines distinct roles for Technical, IP, Security, and Compliance reviewers. Sandbox boundaries prevent developers from viewing internal deliberations while surfacing actionable remediations.
- **Automated Gateway Blocking**: The system physically prevents Final Approval if critical security findings or compliance policy rules are unresolved, acting as an immutable guardrail against human error.
- **Remediation Lifecycle**: Connects developer fixes to follow-up analysis snapshots, allowing seamless re-evaluation cycles.

## Phase 7: Licensing, Agreements & Contract Lifecycle

Phase 7 introduces the legal and commercial abstraction framework, bridging technical repository ownership with legally sound, non-exclusive market availability.
- **Contract Orchestration**: Enforces non-exclusive terms structurally. Active terms are immutable, meaning any changes spawn versioned amendments. 
- **KYC & Signature Guardrails**: Projects logically cannot reach the `ACTIVE` agreement state until the requesting `Organization` is fully verified and cryptographic (abstracted) `SignatureRequest` criteria are met.
- **Decimals & Negotiation**: Financial pricing models strictly utilize `DecimalField` for calculation safety. The `NegotiationProposal` framework securely tracks multi-party counteroffers.

## Phase 8: Finance, KYC, Payouts & Revenue Management

Phase 8 acts as the mathematically airtight transaction orchestrator, processing revenue and paying out creators while avoiding any floating-point liabilities.
- **Double-Entry Engine**: Transactions are atomic and only commit if debits explicitly match credits across logical `LedgerAccount`s.
- **Idempotency Execution**: Concurrency-safe APIs ignore duplicate transaction intents relying on uniquely enforced `idempotency_key`s.
- **Verification Blocking**: The system explicitly halts payout processing if the attached entity lacks full organizational KYC verifications from the prior Phase.

## Phase 9: Administration, Analytics, Reporting & Platform Operations

Phase 9 establishes the operational hub for platform administrators, securely decoupled from user-facing surfaces.
- **Time-Series Analytics**: To circumvent heavy N+1 queries during admin panel loads, background aggregators pre-compute daily `PlatformMetric`s (Active Devs, Gross Revenue) into static rows.
- **Operational Safety**: Health APIs expose database metrics safely. Feature Flags and System Configurations provide zero-downtime control over application routes and business logic limits (e.g., minimum LOC thresholds).

## Requirements

- Python 3.11+
- PostgreSQL 14+ (for production)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CodeVault
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Copy `.env.example` to `.env` and fill in the required values.
   ```bash
   cp .env.example .env
   ```
   > **Important**: Never commit your `.env` file or hardcode secrets in the repository!

5. **Database Setup (Local)**
   By default, local development uses SQLite (as defined in `.env.example`).
   Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/api/v1/`.

## Running Tests

CodeVault uses `pytest`. To run the test suite:
```bash
pytest
```
This will automatically reuse the database for faster subsequent runs.

## Development Conventions

- **Type Hints**: Use Python type hints where practical.
- **Modularity**: Place logic in the appropriate domain app. Do not create circular dependencies.
- **Error Handling**: Use the standardized `core.exceptions.custom_exception_handler` through DRF.
- **Logging**: Use the pre-configured Python `logging` module.

## Security Guidelines

- CodeVault enforces strict security measures. 
- API endpoints are protected by role-based access control (RBAC). 
- Do not expose PII or real credentials.
- Ensure all queries are parameter-safe (handled natively by Django ORM).
