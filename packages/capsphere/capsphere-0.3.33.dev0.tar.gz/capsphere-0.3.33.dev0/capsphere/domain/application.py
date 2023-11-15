from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class BusinessOwnerApplication:
    id: int
    bo_no: str
    bo_first_name: str
    bo_last_name: str
    user_id: int
    bo_business_name: str
    bo_identification_card_number: str
    bo_date_of_birth: datetime
    bo_gender: str
    bo_personal_street: str
    bo_personal_city: str
    bo_personal_state: str
    bo_personal_zipcode: str
    bo_personal_country: str
    bo_personal_phone_country_code: Optional[str]
    bo_personal_phonenumber: int
    bo_business_street: str
    bo_business_city: str
    bo_business_state: str
    bo_business_zipcode: str
    bo_business_country: str
    bo_registered_street: Optional[str]
    bo_registered_city: Optional[str]
    bo_registered_state: Optional[str]
    bo_registered_zipcode: Optional[str]
    bo_registered_country: Optional[str]
    bo_business_phone_country_code: Optional[int]
    bo_business_phonenumber: int
    bo_industry: str
    bo_legal_entity: str
    bo_company_activities: Optional[str]
    existing_approved_limit_amount: Optional[float]
    existing_approved_limit_date: Optional[datetime]
    new_approved_limit_amount: Optional[float]
    new_approved_limit_date: Optional[datetime]
    bo_no_of_employees: int
    bo_no_of_customers_per_year: int
    bo_registration_number: str
    bo_registration_year: int
    bo_court_judgement: str
    bo_court_judgement_yes: Optional[str]
    bo_bank_name: str
    bo_bank_account: int
    bo_agree_terms: bool
    bo_agree_fees: bool
    bo_app_status: str
    bo_status: str
    bo_remark: Optional[str]
    created_at: datetime
    updated_at: datetime
