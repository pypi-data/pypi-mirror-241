from dataclasses import dataclass


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
    due_date: str
    created_at: str
    updated_at: str
    loan_payment_id: int
