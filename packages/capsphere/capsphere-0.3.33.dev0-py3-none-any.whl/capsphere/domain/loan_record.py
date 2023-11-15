from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class LoanRecord:
    id: int
    loan_ref_code: str
    loan_interest_rate: float
    is_stopping_late_fee: int
    stopping_late_fee_date: date
    loan_purpose: str = None
    financing_type: str = None
    loan_type: str = None
    loan_duration: int = None
    created_by: str = None
    user_id: int = None
    require_direct_debit: int = None
    updated_by: str = None
    loan_simple_interest_rate: float = None
    loan_status: str = None
    manager_investment_notes: str = None
    bo_investment_notes: str = None
    loan_funded_percent: float = None
    loan_funded_amount: float = None
    business_owner_application_id: int = None
    loan_asset_type: str = None
    loan_asset_brand: str = None
    loan_asset_model_number: str = None
    loan_asset_url: str = None
    loan_asset_supplier_name: str = None
    loan_asset_purchase_price: int = None
    loan_asset_purchase_number: int = None
    loan_asset_useful_life: int = None
    loan_asset_secondary_market: str = None
    loan_asset_secondary_market_yes: str = None
    loan_asset_salvage: int = None
    loan_guarantor_name: str = None
    loan_guarantor_nric: str = None
    loan_guarantor_mobile: str = None
    loan_guarantor_email: str = None
    loan_guarantor_address: str = None
    loan_guarantor_relationship: str = None
    loan_guarantor_checkbox: int = None
    bo_approved_for_listing: str = None
    bo_approved_for_issuance: str = None
    loan_disbursed_status: str = None
    loan_listing_duration: int = None
    loan_service_fee: float = None
    loan_stamping_fee: float = None
    loan_charge_fee: float = None
    loan_success_fee: float = None
    loan_bank_charges: float = None
    loan_sst: str = None
    loan_remark: str = None
    loan_factsheet: str = None
    created_at: datetime = None
    updated_at: datetime = None
    active: int = None
    loan_category: str = None
    is_shariah: int = None
    is_esg: int = None
    is_guaranteed: int = None
    guaranteed_entity: str = None
    note_listed_at: datetime = None
    publish_date_at: datetime = None
    investor_fee: float = None
    approved_note_status: str = None
    loan_asset_supplier_contact_no: str = None
    credit_rating: str = None
    funded_noti_at: datetime = None
    full_funded_noti_at: datetime = None
    basic_wait_option: int = None
    basic_wait_days: int = None
    basic_wait_percent: int = None
    set_mycif_investment_portion: int = None
    mycif_investment_portion: float = None