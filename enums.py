from enum import Enum


class AssetType(str, Enum):
    equity = "equity"
    etf = "etf"
    bond = "bond"
    reit = "reit"
    private_company = "private_company"
    crypto = "crypto"
    other = "other"


class LifecycleStatus(str, Enum):
    candidate = "candidate"
    research = "research"
    governance = "governance"
    valuation = "valuation"
    committee = "committee"
    certified = "certified"
    monitoring = "monitoring"
    archived = "archived"


class CertificationStatus(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    conditionally_certified = "conditionally_certified"
    certified = "certified"
    expired = "expired"
    rejected = "rejected"


class ValidationStatus(str, Enum):
    pending = "pending"
    validated = "validated"
    rejected = "rejected"
    needs_review = "needs_review"
