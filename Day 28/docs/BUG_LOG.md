# Day 27 Bug and Review Log

| ID | Finding | Resolution / status |
|---|---|---|
| FF-027-01 | Backend requirements file contained escaped newline text, which could make pip treat two requirements as one invalid line. | Fixed: each dependency is now a separate line. |
| FF-027-02 | Frontend `App.jsx` began with an unexpected standalone backslash. | Removed the stray character. |
| FF-027-03 | Nginx proxy path could rewrite `/api/v1/...` to `/v1/...` when forwarding to FastAPI. | Fixed proxy configuration to preserve the original request URI. |
| FF-027-04 | API behavior had schema tests but no endpoint-level regression tests. | Added API tests for health, category CRUD, transaction create/search/filter, validation, and 404 behavior. |
| FF-027-05 | Deployment setup and API usage guidance were incomplete. | Added Dockerfiles, Docker Compose, API reference, architecture, deployment, and screenshot guidance. |

## Verification status

- Backend test command: `python -m pytest -q`
- Result in the build environment: **9 passed**.
- Frontend npm dependency installation/build: **not verified in this environment**; run `npm install` and `npm run build` locally or let the included CI workflow execute.
- Docker image build and live deployment: **not executed**.
- GitHub push: **not performed**; follow the README submission commands.
