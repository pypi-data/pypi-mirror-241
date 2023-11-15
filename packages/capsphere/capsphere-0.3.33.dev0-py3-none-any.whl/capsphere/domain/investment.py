from dataclasses import dataclass
from datetime import datetime


@dataclass
class Investment:
    id: int
    invested_amount: float
    created_by: str
    updated_by: str
    investor_application_id: int
    loan_id: int
    invested_amount_percent: float
    created_at: datetime
    updated_at: datetime
