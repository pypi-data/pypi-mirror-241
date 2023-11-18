from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class LoanRecord:
    id: int
    loan_ref_code: str
    loan_interest_rate: float
    is_stopping_late_fee: int
    stopping_late_fee_date: Optional[str] = None
    loan_purpose: Optional[str] = None
    financing_type: Optional[str] = None
    loan_type: Optional[str] = None
    loan_duration: Optional[int] = None
    created_by: Optional[str] = None
    user_id: Optional[int] = None
    require_direct_debit: Optional[int] = None
    updated_by: Optional[str] = None
    loan_simple_interest_rate: Optional[float] = None
    loan_status: Optional[str] = None
    manager_investment_notes: Optional[str] = None
    bo_investment_notes: Optional[str] = None
    loan_funded_percent: Optional[float] = None
    loan_funded_amount: Optional[float] = None
    business_owner_application_id: Optional[int] = None
    loan_asset_type: Optional[str] = None
    loan_asset_brand: Optional[str] = None
    loan_asset_model_number: Optional[str] = None
    loan_asset_url: Optional[str] = None
    loan_asset_supplier_name: Optional[str] = None
    loan_asset_purchase_price: Optional[int] = None
    loan_asset_purchase_number: Optional[int] = None
    loan_asset_useful_life: Optional[int] = None
    loan_asset_secondary_market: Optional[str] = None
    loan_asset_secondary_market_yes: Optional[str] = None
    loan_asset_salvage: Optional[int] = None
    loan_guarantor_name: Optional[str] = None
    loan_guarantor_nric: Optional[str] = None
    loan_guarantor_mobile: Optional[str] = None
    loan_guarantor_email: Optional[str] = None
    loan_guarantor_address: Optional[str] = None
    loan_guarantor_relationship: Optional[str] = None
    loan_guarantor_checkbox: Optional[int] = None
    bo_approved_for_listing: Optional[str] = None
    bo_approved_for_issuance: Optional[str] = None
    loan_disbursed_status: Optional[str] = None
    loan_listing_duration: Optional[int] = None
    loan_service_fee: Optional[float] = None
    loan_stamping_fee: Optional[float] = None
    loan_charge_fee: Optional[float] = None
    loan_success_fee: Optional[float] = None
    loan_bank_charges: Optional[float] = None
    loan_sst: Optional[str] = None
    loan_remark: Optional[str] = None
    loan_factsheet: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    active: Optional[int] = None
    loan_category: Optional[str] = None
    is_shariah: Optional[int] = None
    is_esg: Optional[int] = None
    is_guaranteed: Optional[int] = None
    guaranteed_entity: Optional[str] = None
    note_listed_at: Optional[str] = None
    publish_date_at: Optional[str] = None
    investor_fee: Optional[float] = None
    approved_note_status: Optional[str] = None
    loan_asset_supplier_contact_no: Optional[str] = None
    credit_rating: Optional[str] = None
    funded_noti_at: Optional[str] = None
    full_funded_noti_at: Optional[str] = None
    basic_wait_option: Optional[int] = None
    basic_wait_days: Optional[int] = None
    basic_wait_percent: Optional[int] = None
    set_mycif_investment_portion: Optional[int] = None
    mycif_investment_portion: Optional[float] = None
