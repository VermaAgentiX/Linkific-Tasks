# Deployment Preparation

This repository includes Dockerfiles for the FastAPI backend and React frontend, plus a Docker Compose setup with PostgreSQL. The setup is intended for local deployment rehearsal and as a starting point for a hosted environment.

## Local Docker rehearsal

From the project root:

```bash
cp .env.example .env
# Edit .env and set a strong POSTGRES_PASSWORD

docker compose up --build
```

Open `http://localhost:8080`. The Nginx container serves the React build and proxies `/api/` requests to the backend. PostgreSQL data is stored in the named `financeflow_data` volume.

Stop the stack:

```bash
docker compose down
```

Remove the database volume only when you intentionally want to delete the local database:

```bash
docker compose down -v
```

## Deployment checklist before a public release

- [ ] Add authentication and server-side authorization.
- [ ] Enforce user/workspace ownership on every data query and mutation.
- [ ] Add Alembic migrations and run them as a controlled release step.
- [ ] Store secrets in the hosting provider's secret manager; never commit `.env`.
- [ ] Set production CORS origins to the exact frontend domain(s).
- [ ] Terminate TLS/HTTPS at the platform or reverse proxy.
- [ ] Configure database backups, retention, and restore tests.
- [ ] Add structured logs, monitoring, and error reporting.
- [ ] Add rate limiting and request-size limits at the edge/API layer.
- [ ] Review dependency vulnerabilities and pin tested versions.
- [ ] Add CI to run backend tests and frontend build on each pull request.
- [ ] Use synthetic data for demos; do not use real financial/customer records during testing.

## Platform notes

### Backend platforms

The backend can be deployed to a container-capable platform. Configure `DATABASE_URL` using the provider's PostgreSQL connection string and set `CORS_ORIGINS` to the frontend origin. The API listens on port `8000` in the included Dockerfile.

### Frontend platforms

The frontend can be deployed as a static Vite build. Set `VITE_API_URL` at build time to the API base URL, including `/api/v1`. For the included Docker/Nginx setup, it is set to `/api/v1` and API requests are reverse-proxied to the backend service.

## Current limitations

The API currently calls `Base.metadata.create_all()` during startup. This is convenient for a local learning project, but it is not a replacement for Alembic migrations. The included Docker Compose file is a deployment-preparation baseline, not a claim that the app is production-secure or already hosted.
