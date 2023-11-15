from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional


@dataclass
class LoanAmortization:
    id: int = None
    loan_id: int = None
    monthly_payment: float = 0.00
    total_amount_paid: float = 0.00
    principal_paid: float = 0.00
    amount_remaining: float = 0.00
    interest_amount: float = 0.00
    due_date: date = None
    paid_status: Optional[str] = None
    month: int = None
    created_by: str = None
    updated_by: str = None
    created_at: datetime = None
    updated_at: datetime = None
