from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class LoanPayment:
    id: int
    loan_amount_paid: float
    prepayment_fee: Optional[float]
    loan_payment_ref_no: str
    loan_payment_processing_fee: int
    loan_paid_uid: str
    fpx_mode: Optional[str]
    loan_amount_verified: Optional[str]
    loan_payment_status: Optional[str]
    approved_at: Optional[datetime]
    loan_id: int
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime
    loan_payment_type: str
    manual_payment_proof_file: Optional[str]
    created_by_id: int
    updated_by_id: int
    is_prepayment: int
