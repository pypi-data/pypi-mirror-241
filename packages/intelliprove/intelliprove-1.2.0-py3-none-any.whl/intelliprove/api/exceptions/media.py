from intelliprove.api.models.enums import QualityErrorType
from typing import Union
from pathlib import Path

from intelliprove.api.models.responses.unprocessable_video_response import UnprocessableVideoResponse


class ImageQualityException(Exception):
    # message, quality error code, score
    def __init__(self, message: str, error_type: QualityErrorType, score: int):
        super().__init__()
        self.message = message
        self.error_type = error_type
        self.score = score

    def __str__(self):
        return f"Image Quality Exception: {self.message}."


class MediaException(Exception):
    # reason, filepath
    def __init__(self, reason: str, filepath: Union[str, Path]):
        super().__init__()
        self.filepath = filepath
        self.reason = reason

    def __str__(self):
        return f"Media Exception: {self.reason} for file '{self.filepath}'."

class VideoProcessingFailedException(Exception):
    def __init__(self, response: UnprocessableVideoResponse, *args: object) -> None:
        super().__init__(*args)
        self.response = response

    def __str__(self) -> str:
        return f"VideoProcessingFailedException with code {self.response.error_code} {': ' + self.response.error_description if self.response.error_description != '' else ''}"

