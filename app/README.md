# FinanceFlow AI 💸
### Smart Personal & Small Business Financial Management Platform

**FinanceFlow AI** is an AI-powered financial management web application designed to help individuals and small business owners organize their income, expenses, transactions, customer credit, supplier payments, and financial activities in one place.

The platform combines personal finance management and small-business financial tracking with AI-powered insights to make everyday financial management simpler and more accessible.

> 🚧 **Project Status:** Planning & Development — Day 22

---

## 🎯 Project Vision

To build a user-friendly financial management platform that helps people understand where their money goes, manage outstanding payments, and make better financial decisions using organized financial data and AI assistance.

## 💡 Problem Statement

Individuals and small business owners often manage their financial activities using notebooks, spreadsheets, or multiple disconnected applications.

This creates challenges such as:

- Difficulty tracking daily income and expenses.
- Lack of visibility into monthly spending patterns.
- Forgetting customer credit (Udhaar) and outstanding payments.
- Difficulty tracking supplier payments.
- Time-consuming manual financial calculations.
- Lack of meaningful financial insights.

**FinanceFlow AI aims to solve these problems** through a centralized platform for personal and business financial management.

## ✨ Planned Features

### 1. Personal Finance Management

- Track daily income and expenses.
- Categorize financial transactions.
- Create monthly budgets.
- Monitor savings and spending patterns.
- View transaction history.
- Analyze monthly financial summaries.

### 2. Small Business Finance Management

Designed for stationery shops, medical stores, small retailers, and other local businesses.

- Record daily sales and business expenses.
- Manage customer information.
- Track customer credit (Udhaar).
- Maintain customer payment history.
- Manage supplier information.
- Track pending supplier payments.
- Monitor business cash flow.

### 3. AI Financial Assistant

- AI-powered transaction category suggestions.
- Natural-language financial queries.
- Monthly financial summaries.
- Spending pattern analysis.
- Identification of unusual spending.
- Context-aware financial insights based on recorded transactions.

### 4. Dashboard & Analytics

- Total income.
- Total expenses.
- Available balance.
- Monthly financial overview.
- Customer outstanding payments.
- Supplier outstanding payments.
- Interactive financial charts.
- Recent transaction history.

---

## 🖥️ Technology Stack

| Layer | Technology |
|---|---|
| UI/UX Design | Figma |
| Frontend | React.js + Vite |
| Styling | Tailwind CSS |
| UI Components | DaisyUI |
| Backend | Python FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database Migrations | Alembic |
| Authentication | JWT |
| AI Workflow | LangGraph |
| AI Model | LLM API / Local LLM |
| Data Visualization | Recharts |
| API Testing | Postman |
| Code Editor | VS Code |
| Version Control | Git & GitHub |

## 🏗️ System Architecture

```text
                 USER
                   |
                   ▼
          REACT FRONTEND
             (Vite)
                   |
          Tailwind + DaisyUI
                   |
                   ▼
             FASTAPI
              BACKEND
                   |
       ┌───────────┴───────────┐
       |                       |
       ▼                       ▼
  PostgreSQL              AI MODULE
   DATABASE               LangGraph
       |                       |
       ▼                       ▼
  SQLAlchemy             LLM / AI Tools
       |                       |
       └───────────┬───────────┘
                   |
                   ▼
             USER RESPONSE
```

**Architecture principle:** FastAPI will handle application logic and financial calculations. LangGraph will orchestrate AI-assisted workflows. Financial balances and totals will always be calculated using actual database records rather than relying on LLM-generated numbers.

## 🔄 Application Workflow

```text
User Registration / Login
          |
          ▼
    Authentication
          |
          ▼
   Workspace Selection
          |
     ┌────┴─────┐
     ▼          ▼
  Personal    Business
  Finance     Finance
     |          |
     ▼          ▼
 Transactions  Sales & Expenses
 Budgets       Customers
 Analytics     Suppliers
     |          |
     └────┬─────┘
          |
          ▼
    PostgreSQL
          |
          ▼
    AI Assistant
     LangGraph
          |
          ▼
 Financial Insights
```

## 🗄️ Planned Database Schema

The application will use PostgreSQL with a relational database architecture.

| Table | Purpose |
|---|---|
| `users` | User accounts and authentication |
| `workspaces` | Personal and business workspaces |
| `categories` | Income and expense categories |
| `transactions` | Financial transaction records |
| `budgets` | Monthly budget management |
| `customers` | Business customer information |
| `customer_ledger_entries` | Customer credit and payment history |
| `suppliers` | Supplier information |
| `supplier_ledger_entries` | Supplier purchase and payment history |
| `ai_conversations` | AI assistant conversation metadata |
| `ai_messages` | AI conversation messages |

### Database Relationships

- One user can own multiple workspaces.
- One workspace can contain multiple transactions.
- One workspace can contain multiple categories and budgets.
- One business workspace can manage multiple customers.
- One customer can have multiple ledger entries.
- One business workspace can manage multiple suppliers.
- One supplier can have multiple ledger entries.

Customer and supplier outstanding balances will be derived from their respective ledger entries.

## 📁 Planned Project Structure

```text
FinanceFlow-AI/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── app/
│       ├── components/
│       │   ├── ui/
│       │   ├── charts/
│       │   └── feedback/
│       ├── features/
│       │   ├── auth/
│       │   ├── workspaces/
│       │   ├── dashboard/
│       │   ├── transactions/
│       │   ├── budgets/
│       │   ├── customers/
│       │   ├── suppliers/
│       │   ├── ai-insights/
│       │   ├── reports/
│       │   └── settings/
│       ├── layouts/
│       ├── services/
│       ├── hooks/
│       ├── utils/
│       ├── styles/
│       └── main.jsx
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── endpoints/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── ai/
│   │   │   ├── graph.py
│   │   │   ├── state.py
│   │   │   ├── nodes.py
│   │   │   ├── tools.py
│   │   │   └── prompts.py
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
│
├── docs/
│   ├── PROJECT_BLUEPRINT.md
│   ├── USER_FLOWS.md
│   ├── DATABASE_SCHEMA.md
│   ├── API.md
│   └── screenshots/
│
├── .github/
│   └── workflows/
│
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## 🗓️ Development Roadmap

The initial development plan covers seven days.

| Day | Task | Planned Deliverable |
|---|---|---|
| Day 22 | Project Ideation & Planning | Project proposal, workflows, database design, roadmap |
| Day 23 | Project Initialization & UI Design | GitHub repository, React/FastAPI setup, Figma design |
| Day 24 | Database & Authentication | PostgreSQL, SQLAlchemy, Alembic, JWT authentication |
| Day 25 | Dashboard & UI Components | Responsive dashboard and reusable React components |
| Day 26 | Personal Finance Module | Income, expenses, categories, budgets |
| Day 27 | Business Finance Module | Sales, customers, Udhaar, suppliers |
| Day 28 | AI Assistant & Analytics | LangGraph workflows and financial insights |
| Day 29 | Integration & Testing | Bug fixing, documentation, deployment preparation |

## 🔐 Security & Privacy

Security will be considered throughout development.

- JWT-based authentication.
- Secure password hashing.
- Protected API endpoints.
- User-specific workspace access.
- Input validation and structured error handling.
- Environment-based secret management.
- Database access restrictions.
- Read-only AI tools for financial analysis.

## 🚀 Future Enhancements

Potential future features include:

- Receipt scanning using OCR.
- Automatic transaction categorization.
- Invoice and PDF report generation.
- Recurring transaction management.
- Inventory integration for small businesses.
- Financial forecasting.
- Payment reminders.
- Mobile-friendly Progressive Web App.
- Regional language support.

## 🛠️ Initial Setup

The following setup commands are planned for project initialization.

### Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/FinanceFlow-AI.git
cd FinanceFlow-AI
```

### Frontend setup

```bash
cd frontend
npm install
npm run dev
```

### Backend setup

```bash
cd backend
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Database configuration

Create a PostgreSQL database and configure backend environment variables in `backend/.env`.

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/financeflow
SECRET_KEY=your_secure_secret_key
```

*These commands and configuration are setup targets; update them to match the actual implementation as development progresses.*

## 🧪 Testing Strategy

Planned testing tools and activities:

- Postman for REST API testing.
- Pytest for backend tests.
- FastAPI TestClient for endpoint testing.
- React Testing Library for frontend components.
- PostgreSQL queries for database verification.
- Manual testing of personal and business workflows.
- Authorization and data-isolation tests.

## 📌 Project Status

🚧 **Currently in the Planning Phase**

- [x] Project idea finalized.
- [x] Problem statement defined.
- [x] Target users identified.
- [x] MVP features planned.
- [x] User stories prepared.
- [x] Application workflow designed.
- [x] Initial database schema proposed.
- [x] Technology stack selected.
- [x] Development roadmap prepared.
- [ ] Figma UI prototype.
- [ ] Frontend implementation.
- [ ] Backend implementation.
- [ ] Database integration.
- [ ] AI integration.
- [ ] Testing and deployment.

## 👨‍💻 Development

**Project:** FinanceFlow AI  
**Category:** AI-Powered Financial Management  
**Development:** Internship / Self-learning Project  
**Repository:** `FinanceFlow-AI`

---

*FinanceFlow AI — Making everyday financial management simpler, smarter, and more accessible.*
