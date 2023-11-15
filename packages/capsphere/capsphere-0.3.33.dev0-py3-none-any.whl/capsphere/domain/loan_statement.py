from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class LoanStatement:
    loan_id: int
    amort_id: int
    month: int
    interest: float
    principal: float
    due_date: date
    id: int = 0
    amount_paid: float = 0.00
    os_late_interest: float = 0.00
    os_late_interest_paid: float = 0.00
    os_late_interest_short: float = 0.00
    os_interest: float = 0.00
    os_interest_paid: float = 0.00
    os_interest_short: float = 0.00
    current_interest_paid: float = 0.00
    current_interest_short: float = 0.00
    total_interest_short: float = 0.00
    os_principal: float = 0.00
    os_principal_paid: float = 0.00
    os_principal_short: float = 0.00
    current_principal_paid: float = 0.00
    current_principal_short: float = 0.00
    total_principal_short: float = 0.00
    current_late_interest: float = 0.00
    overdue_days: int = 0.00
    current_late_interest_paid: float = 0.00
    partial_interest: float = 0.00
    partial_interest_discount: float = 0.00
    total_late_interest: float = 0.00
    next_payment_amount: float = 0.00
    pay_before_due: int = 1
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def update(self, field_name, new_value):
        if hasattr(self, field_name):
            setattr(self, field_name, new_value)
        else:
            print(f"Field '{field_name}' does not exist in the dataclass")
