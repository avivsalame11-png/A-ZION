from datetime import datetime
from pydantic import BaseModel, Field


class DomainEvent(BaseModel):
    event_type: str
    entity_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source: str = "A-ZION"
    payload: dict = Field(default_factory=dict)
