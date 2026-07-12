from fastapi import APIRouter, HTTPException
from core.evidence.schemas import EvidenceCreate, EvidenceRead, EvidenceValidate

router = APIRouter()

_EVIDENCE: dict[str, EvidenceRead] = {}


@router.post("", response_model=EvidenceRead)
def create_evidence(payload: EvidenceCreate) -> EvidenceRead:
    if payload.evidence_id in _EVIDENCE:
        raise HTTPException(status_code=409, detail="evidence_id already exists")
    evidence = EvidenceRead(**payload.model_dump())
    _EVIDENCE[payload.evidence_id] = evidence
    return evidence


@router.get("/{evidence_id}", response_model=EvidenceRead)
def get_evidence(evidence_id: str) -> EvidenceRead:
    evidence = _EVIDENCE.get(evidence_id)
    if not evidence:
        raise HTTPException(status_code=404, detail="Evidence not found")
    return evidence


@router.patch("/{evidence_id}/validate", response_model=EvidenceRead)
def validate_evidence(evidence_id: str, payload: EvidenceValidate) -> EvidenceRead:
    evidence = _EVIDENCE.get(evidence_id)
    if not evidence:
        raise HTTPException(status_code=404, detail="Evidence not found")
    updated = evidence.model_copy(update={"validation_status": payload.validation_status})
    _EVIDENCE[evidence_id] = updated
    return updated
