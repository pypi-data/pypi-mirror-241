from pydantic.dataclasses import dataclass
from datetime import datetime, date
from typing import Optional


@dataclass
class LoanAmortization:
    id: int
    loan_id: int
    month: int
    created_by: str
    updated_by: str
    monthly_payment: float = 0.00
    total_amount_paid: float = 0.00
    principal_paid: float = 0.00
    amount_remaining: float = 0.00
    interest_amount: float = 0.00
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    paid_status: Optional[str] = None
