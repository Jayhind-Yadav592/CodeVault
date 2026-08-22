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

## Phase 10: Integration Platform, Webhooks & Developer API

Phase 10 transforms CodeVault into an extensible ecosystem safely communicating with the outside world.
- **Secure Scoped API**: Developer API tokens are irreversibly hashed at creation. Interactions enforce granular scopes (`projects:read`, `webhooks:write`) and throttle limits.
- **Webhooks & SSRF Defenses**: Emitted events traverse a cryptographic HMAC-SHA256 signature process before payload delivery. Endpoints are aggressively filtered for Server-Side Request Forgery (SSRF) to shield internal architectures.

## Phase 11: Advanced Testing, Performance, Reliability & Production Hardening

Phase 11 transformed CodeVault into an enterprise-ready system capable of handling high loads, maintaining absolute ledger integrity, and orchestrating reproducible deployments.
- **Concurrency Defenses**: Database row-level locking (`select_for_update()`) strictly enforced across all payment rails and wallet mutations, eliminating double-spend race conditions.
- **Query Optimization**: N+1 bottlenecks purged from API viewsets and dashboard rendering templates via deliberate `select_related()` graphs.
- **CI/CD Pipeline**: GitHub Actions automatically govern code pushes—running type checks, migration verifications, and Pytest suites against a Postgres matrix.
- **System Diagnostics**: Built-in CLI operations (`manage.py system_diagnostics`) provide administrators instantaneous audits over double-entry ledger equilibrium and data orphan status.

## Phase 12: Discovery, Search, Marketplace & Recommendation Engine

CodeVault incorporates a robust, privacy-respecting **Marketplace** that allows licensees to discover verified repositories:
- **Publication Gate**: A strict validator (`PublicationService`) guarantees that only `APPROVED` projects with signed IP ownership and zero critical security findings (like exposed secrets) can be transitioned to a `PUBLISHED` marketplace listing.
- **Secure Discovery Index**: The `/api/v1/marketplace/listings/` endpoint powers exact, partial, and faceted searches (by language, category, LOC, and tags). It runs exclusively against the `MarketplaceListing` entity, structurally isolating and hiding any `PRIVATE` or `UNLISTED` draft projects.
- **Explainable Recommendations**: A rule-based engine generates customized project recommendations by analyzing a developer's explicit `SavedProject` portfolio. Each suggestion returns a discrete `recommendation_reason` without relying on black-box AI logic.
- **Analytics & Curation**: Supports user-curated `Watchlist`s and `SavedProject` folders. Features asynchronous telemetry via `SearchQueryLog` to identify "Zero-Result Searches", letting administrators spot unserved market demands.

## Phase 13: Team Collaboration, Developer Workspace & Project Operations

A robust internal collaborative workspace mapping technical operators to project deliverables while maintaining a fierce separation from legal intellectual property logic.
- **Organization & Role Sandboxing**: Supports multi-tenant organizational structure with encrypted, time-bounded member invitations and discrete role assignments (Owner, Admin, Member) that strictly bound system access limits.
- **Integrated Project Ops**: Houses native `ProjectTasks`, `ProjectMilestones`, and internal `ProjectDiscussions`. Crucially implements explicit **Architecture Decision Records (ADRs)** to preserve contextual memory.
- **Compliance-Aware Releases**: Exposes semantic `ProjectRelease` objects that directly tie abstract version numbers (e.g., v1.4) back to a mathematically immutable Git `AnalysisSnapshot`.
- **Security Boundaries**: Protected comprehensively by custom DRF Permission blocks (`IsProjectMember`, `IsOrganizationAdmin`) guaranteeing Absolute IDOR (Insecure Direct Object Reference) isolation across projects.

## Phase 14: AI Repository Intelligence & ML Evaluation Platform

CodeVault features a modular AI/ML subsystem that enforces dataset integrity and absolute decision transparency, avoiding black-box assertions.
- **Explainable AI Pipeline**: Introduces immutable `FeatureVector`s parsed deterministically from Git and Compliance operations. Every `Prediction` persists an `explanation` payload mapping directly back to contributing features (e.g., test ratio or security findings count).
- **Anti-Leakage Data Management**: The `DatasetSplit` topology enforces absolute boundaries between `TRAIN`, `VALIDATION`, and `TEST` sets at the ORM level, guaranteeing test-set contamination cannot occur natively.
- **Strict Model Promotion Workflow**: `ModelRegistry` records enforce a strict lifecycle (`EXPERIMENT` -> `PRODUCTION`). The `InferenceService` structurally rejects any attempts to compute predictions utilizing non-production models.
- **Anti-Hallucination Constraints**: The integrated `ReviewAssistantService` generates human-readable repository summaries using direct deterministic bindings to the underlying database rather than generative language models, preventing hallucinatory claims.

## Phase 15: Enterprise Governance, Risk & Policy Management

CodeVault features a full GRC (Governance, Risk, and Compliance) layer permitting organizations to manage risk and enforce policies without tangling compliance logic directly into codebase operations.
- **Immutable Policy Lifecycle**: The `PolicyWorkflowService` ensures that once a `PolicyVersion` reaches `ACTIVE` status, it cannot be modified. Historical `ControlEvaluation`s retain references to the exact policy active at that point in time.
- **Time-Bounded Exceptions**: The `ExceptionManagerService` strictly enforces expiration dates on policy exceptions. Upon expiration, a control automatically downgrades to failing, preventing temporary waivers from becoming permanent backdoors.
- **Evidence-Based Evaluation**: Controls (`Control`) and their corresponding outcomes (`ControlEvaluation`) map many-to-many to concrete `Evidence` artifacts (like a security scan ID or manual reviewer approval). This structure avoids claiming regulatory compliance off simple automated tests alone.
- **Deterministic Risk Engine**: The `Risk` register computes straightforward deterministic scores (Likelihood * Impact) rather than relying on obfuscated algorithms, enabling transparent risk treatment (Mitigate, Accept, Transfer, Avoid).

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
