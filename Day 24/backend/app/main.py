from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import Base, engine
from app import models  # noqa: F401 - register model metadata
from app.api.routes.crud_routes import router as crud_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Day 24 convenience only; use Alembic migrations in production.
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok", "service": "FinanceFlow AI API"}

app.include_router(crud_router, prefix=settings.api_v1_prefix)
