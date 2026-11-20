"""API-level tests using an isolated SQLite database."""
from datetime import date

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app
from app import models  # noqa: F401 - register SQLAlchemy models


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(bind=engine)

    def override_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


def test_health_endpoint(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_read_category(client):
    created = client.post("/api/v1/categories", json={"name": "Food", "kind": "expense"})
    assert created.status_code == 201
    category_id = created.json()["id"]

    fetched = client.get(f"/api/v1/categories/{category_id}")
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "Food"


def test_transaction_create_filter_and_search(client):
    payload = {
        "title": "Office rent", "amount": "8500.00", "type": "expense",
        "date": date.today().isoformat(), "payment_method": "bank", "account": "Main account"
    }
    created = client.post("/api/v1/transactions", json=payload)
    assert created.status_code == 201
    assert created.json()["amount"] == "8500.00"

    filtered = client.get("/api/v1/transactions", params={"q": "rent", "type": "expense", "limit": 10})
    assert filtered.status_code == 200
    assert len(filtered.json()) == 1

    searched = client.get("/api/v1/transactions/search", params={"q": "office"})
    assert searched.status_code == 200
    assert searched.json()[0]["title"] == "Office rent"


def test_invalid_transaction_is_rejected(client):
    payload = {
        "title": "Bad amount", "amount": "0", "type": "expense",
        "date": date.today().isoformat()
    }
    response = client.post("/api/v1/transactions", json=payload)
    assert response.status_code == 422


def test_missing_record_returns_404(client):
    response = client.get("/api/v1/customers/99999")
    assert response.status_code == 404
