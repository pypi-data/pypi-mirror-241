from typing import Any, Dict
from dataclasses import dataclass


@dataclass
class UnprocessableVideoResponse:
    error_code: int
    error_type: str
    error_description: str = ""

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'UnprocessableVideoResponse':
        return cls(
            error_code=data['errorCode'],
            error_type=data['errorType'],
            error_description=data.get('errorDescription', '')
        )

