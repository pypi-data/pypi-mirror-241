from typing import Optional
from dataclasses import dataclass
from intelliprove.api.models.enums import QualityErrorType


@dataclass
class Quality:
    score: int
    prompt: str
    error_type: QualityErrorType
    signature: Optional[str] = None

