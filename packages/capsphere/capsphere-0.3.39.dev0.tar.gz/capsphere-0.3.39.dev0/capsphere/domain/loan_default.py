from typing import Optional

from pydantic.dataclasses import dataclass

@dataclass
class LoanDefault:
    id: int
    bo_id: int
    loan_id: int
    amount_due: float
    outstanding_principal: float
    outstanding_interest: float
    outstanding_late_fee: float
    amount_recovered: float
    legal_fee: float
    status: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
