from pydantic.dataclasses import dataclass
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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    due_date: Optional[str] = None
    paid_status: Optional[str] = None
