from typing import Any, Dict, Optional
from dataclasses import dataclass
from intelliprove.api.models.enums import QualityErrorType
from intelliprove.api.models.dataclasses import Quality


@dataclass
class QualityResponse:
    score: int
    prompt: str
    error_type: QualityErrorType
    signature: Optional[str] = None

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'QualityResponse':
        return cls(
            score=data['quality_score'],
            prompt=data['prompt'],
            error_type=QualityErrorType(data['quality_error_code']),
            signature=data['signature']
        )

    def to_dataclass(self):
        return Quality(**self.__dict__)

