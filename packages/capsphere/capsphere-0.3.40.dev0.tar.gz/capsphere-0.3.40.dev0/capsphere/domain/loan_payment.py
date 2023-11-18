from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class LoanPayment:
    id: int
    loan_amount_paid: float
    loan_payment_ref_no: str
    loan_payment_processing_fee: int
    loan_paid_uid: str
    fpx_mode: Optional[str]
    loan_id: int
    created_by: str
    updated_by: str
    loan_payment_type: str
    created_by_id: int
    updated_by_id: int
    is_prepayment: int
    manual_payment_proof_file: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    loan_amount_verified: Optional[float] = None
    loan_payment_status: Optional[str] = None
    approved_at: Optional[str] = None
    prepayment_fee: Optional[float] = None
