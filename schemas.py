from enum import Enum
from pydantic import BaseModel, Field
from core.shared.enums import ValidationStatus


class SourceType(str, Enum):
    sec_filing = "sec_filing"
    investor_relations = "investor_relations"
    earnings_release = "earnings_release"
    transcript = "transcript"
    presentation = "presentation"
    market_data = "market_data"
    regulatory = "regulatory"
    internal = "internal"


class EvidenceCreate(BaseModel):
    evidence_id: str = Field(..., examples=["EVD-GR003-0001"])
    asset_id: str
    source_type: SourceType
    source_name: str
    source_url: str | None = None
    document_id: str | None = None
    document_date: str | None = None
    filing_type: str | None = None
    excerpt: str | None = None
    metric_name: str | None = None
    metric_value: str | None = None
    unit: str | None = None
    confidence_score: float = 0.0


class EvidenceRead(EvidenceCreate):
    validation_status: ValidationStatus = ValidationStatus.pending


class EvidenceValidate(BaseModel):
    validation_status: ValidationStatus
    notes: str | None = None
