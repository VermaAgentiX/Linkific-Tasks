from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app import models  # noqa: F401
from app.api.routes.crud_routes import router as crud_router
from app.core.config import settings
from app.core.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.4.0",
    description="FinanceFlow AI REST API — Day 27 tested and documented build",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": [
            {
                "field": ".".join(str(part) for part in err["loc"]),
                "message": err["msg"],
                "type": err["type"],
            }
            for err in exc.errors()
        ]},
    )


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": settings.app_name, "docs": "/docs"}


@app.get("/health", tags=["Health"])
@app.get(f"{settings.api_v1_prefix}/health", tags=["Health"])
def health():
    return {"status": "ok", "service": settings.app_name}


app.include_router(crud_router, prefix=settings.api_v1_prefix)
