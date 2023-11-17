from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class LedgerEntry:
    id: int
    user_id: int
    ledgerable_id: int
    ref_code: str
    reason: str
    credit: int
    debit: int
    amount: float
    balance: float
    due_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    loan_payment_id: int
