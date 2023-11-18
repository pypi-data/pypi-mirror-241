from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class Investment:
    id: int
    invested_amount: float
    created_by: str
    updated_by: str
    investor_application_id: int
    loan_id: int
    invested_amount_percent: float
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
