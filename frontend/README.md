# CodeVault Frontend

The React frontend for the CodeVault platform, built with modern web technologies.

## Tech Stack
- **Framework:** React 19 + TypeScript
- **Bundler:** Vite
- **Routing:** React Router
- **Styling:** Tailwind CSS (via PostCSS)
- **API Client:** Axios
- **Testing:** Vitest + React Testing Library

## Prerequisites
- Node.js (v18 or higher)
- npm (v9 or higher)

## Installation
```bash
npm install
```

## Development
```bash
npm run dev
```
The development server will run at `http://localhost:5173`. 
The frontend expects the Django API to be running at `http://localhost:8000`.

## Environment Variables
Create a `.env` file based on `.env.example`:
- `VITE_API_BASE_URL`: Base URL for the Django REST API.
- `VITE_APP_NAME`: Application title (default: CodeVault)

**SECURITY WARNING:** Never store sensitive API keys, secrets, or passwords in frontend environment variables since they will be embedded into the public build!

## Available Commands
- `npm run dev` - Start development server
- `npm run build` - Create production build
- `npm run lint` - Run ESLint (via oxlint)
- `npm run typecheck` - Run TypeScript compiler checks
- `npm run test` - Run Vitest test suite

## Django Integration
The Django backend has been configured with `django-cors-headers` to accept requests from `http://localhost:5173`. Authentication is handled securely via backend session cookies or DRF tokens depending on your environment.

### Production Deployment Strategy
1. **Option A (Decoupled):** Deploy the `dist/` folder output to a CDN/Static Host (e.g. AWS S3, Vercel) and point `VITE_API_BASE_URL` to the production Django server.
2. **Option B (Monolithic):** Copy the `dist/` folder into Django's static directories and serve the `index.html` via a Django wildcard route.
