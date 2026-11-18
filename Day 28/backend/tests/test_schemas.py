from datetime import date
from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.schemas.resources import BudgetCreate, ContactCreate, TransactionCreate


def test_transaction_rejects_zero_amount():
    with pytest.raises(ValidationError):
        TransactionCreate(title="Invalid", amount=0, type="expense", date=date.today())


def test_transaction_accepts_decimal_amount():
    obj = TransactionCreate(title="Office supplies", amount="125.50", type="expense", date=date.today())
    assert obj.amount == Decimal("125.50")


def test_budget_rejects_end_date_before_start_date():
    with pytest.raises(ValidationError):
        BudgetCreate(name="Monthly", amount="1000",
                     start_date=date(2026, 11, 20), end_date=date(2026, 11, 10))


def test_blank_contact_email_is_normalized_to_none():
    obj = ContactCreate(name="Test customer", email="")
    assert obj.email is None
