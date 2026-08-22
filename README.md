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
