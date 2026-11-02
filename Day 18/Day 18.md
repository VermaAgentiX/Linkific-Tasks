# Day 18 -- Project Optimization & Clean Code

## Student Record Manager

**Internship:** Linkific -- Python Full-Stack Developer\
**Day:** 18\
**Date:** 2 November 2026

------------------------------------------------------------------------

## 1. Overview

Day 18 focused on improving the maintainability and readability of the
Student Record Manager React + FastAPI application. The project was
reviewed and refactored to reduce repeated UI code, improve component
organization, and make the frontend easier to maintain.

## 2. Objectives

-   Refactor repeated code.
-   Improve folder and component organization.
-   Use clear, meaningful names for variables and functions.
-   Remove unnecessary generated or unused files.
-   Improve readability and maintainability.
-   Keep existing application functionality intact.

## 3. Technology Stack

  Technology   Purpose
  ------------ ----------------------------
  React        Frontend components and UI
  JavaScript   Frontend logic
  FastAPI      Backend REST API
  Python       Backend implementation
  PostgreSQL   Database
  SQLAlchemy   Database ORM
  JWT          Authentication

## 4. Refactoring Changes

### Frontend organization

-   Extracted protected application layout and data-loading
    responsibilities into `src/layouts/ProtectedApp.jsx`.
-   Simplified `App.jsx` so it focuses on application routing and
    authentication flow.
-   Added reusable `FormField.jsx` to reduce repeated form-field markup.
-   Kept form validation, error messages, and accessibility attributes
    in the reusable form component.

### Project cleanup

-   Removed generated Python bytecode from the packaged project.
-   Excluded the local SQLite database from the project ZIP.
-   Added `DAY18_REFACTOR_NOTES.md` to document the changes.

## 5. Why These Changes Matter

-   **Reusability:** Shared form-field markup is maintained in one
    component.
-   **Separation of concerns:** Routing and protected application layout
    responsibilities are separated.
-   **Readability:** Smaller components are easier to understand and
    review.
-   **Maintainability:** Future UI changes can be made in one reusable
    component.
-   **Repository hygiene:** Generated artifacts and local database files
    are not included in the project package.

## 6. Run the Application

### Backend

``` powershell
cd backend
uvicorn main:app --reload
```

### Frontend

``` powershell
cd frontend
npm install
npm run build
npm run dev
```

### API documentation

Open <http://127.0.0.1:8000/docs>.

## 7. Verification Checklist

-   [ ] Frontend production build completes successfully.
-   [ ] Login and logout work.
-   [ ] Dashboard and protected routes load correctly.
-   [ ] Student list and search work.
-   [ ] Create and edit student forms validate input.
-   [ ] Student details page loads.
-   [ ] Student deletion works.
-   [ ] Admin-only features remain restricted.
-   [ ] Backend API and PostgreSQL integration work.
-   [ ] Changes are committed and pushed to GitHub.

## 8. Deliverables

-   Refactored React + FastAPI project.
-   Reusable `FormField.jsx` component.
-   Extracted `ProtectedApp.jsx` layout.
-   `DAY18_REFACTOR_NOTES.md`.
-   Updated GitHub repository.

## 9. Learning Outcomes

-   Applied clean-code and component-reuse principles.
-   Improved separation of concerns in a React application.
-   Practiced organizing frontend responsibilities into focused
    components.
-   Learned the value of removing generated artifacts from source
    packages.
-   Improved project readability and maintainability.

------------------------------------------------------------------------

**Day 18 -- Project Optimization & Clean Code**\
*Linkific Python Full-Stack Developer Internship*
