# Day 15 implementation notes

- Public registration creates a normal user unless the email is explicitly listed in `ADMIN_EMAILS`.
- Configure `ADMIN_EMAILS` in `backend/.env` before registering the admin account. Existing matching accounts are promoted on startup.
- Admin-only endpoint: `GET /admin/users`.
- Frontend `/admin` route is restricted to admins; other users are redirected to `/unauthorized`.
- Student CRUD remains scoped by `owner_id`.
- JWT logout is stateless: the browser discards the token, but a copied token remains valid until expiry. Production systems should consider short access-token lifetimes and refresh-token rotation/revocation.
- Do not commit `.env`. The uploaded `.env` was excluded from this archive to avoid sharing local credentials.
- A simple additive migration adds the `role` column to an existing `users` table. Back up data before schema changes.
