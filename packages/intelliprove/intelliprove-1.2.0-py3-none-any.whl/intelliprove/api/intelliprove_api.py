import typing
import logging

from pathlib import Path
from datetime import timedelta
from typing import Optional, Union

from intelliprove.api.api_service import ApiService
from intelliprove.api.exceptions.media import VideoProcessingFailedException
from intelliprove.api.models import IntelliproveApiSettings, Biomarkers, Quality
from intelliprove.api.models.responses import BiomarkersResponse
from intelliprove.api.models.enums import QualityErrorType
from intelliprove.api.models.responses.unprocessable_video_response import UnprocessableVideoResponse
from intelliprove.api.utils import is_valid_video_path, is_valid_image_path, get_first_video_frame, check_file_size
from intelliprove.api.exceptions import ImageQualityException, MediaException, ApiResultNotAvailable


# logging config
logging.basicConfig(
     level=logging.INFO,
     format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
)


class IntelliproveApi:
    def __init__(self, api_key: str, settings: Optional[IntelliproveApiSettings] = None):
        self.api = ApiService(api_key, settings)

    def upload(self, video_file: Path, performer: Optional[str] = None, patient: Optional[str] = None) -> str:
        """
        Upload the video to the API and start the processing.
        Returns: the measurement uuid
        """

        # check video size
        allowed_size = self.api.settings.max_video_size_mb
        size = check_file_size(video_file, 'mb')
        if size > allowed_size:
            raise MediaException(f"Expected video file size to be below {allowed_size} Mb, given video size is {size} Mb.",
                                 video_file)

        # Check first frame of video with api
        quality = self.check_conditions(video_file)
        if quality.error_type != QualityErrorType.NONE:
            raise ImageQualityException("First frame of video does not pass the quality check.", quality.error_type,
                                        quality.score)

        # if error_type is NONE => signature always present
        quality.signature = typing.cast(str, quality.signature)

        logging.info('Media checks done, started uploading...')
        # if check is ok => upload video
        upload_data = self.api.get_upload_url(quality.signature)
        uuid: str = upload_data['uuid']

        self.api.upload_video(video_file, upload_data)

        logging.info('Video upload done, queueing video...')
        self.api.queue_upload(uuid, performer, patient)

        return uuid

    def get_results(self, uuid: str) -> Biomarkers:
        """
        Fetch the results from the API by performing long polling.
        """
        for _ in range(self.api.settings.get_results_retry_count):
            result = self.api.get_result(uuid)
            if isinstance(result, BiomarkersResponse):
                return result.to_dataclass()
            elif isinstance(result, UnprocessableVideoResponse):
                raise VideoProcessingFailedException(result)

        raise ApiResultNotAvailable(uuid)

    def check_conditions(self, snapshot: Path) -> Quality:
        """
        Check the conditions of an image or video file.
        """
        if is_valid_video_path(snapshot):
            frame_path = get_first_video_frame(snapshot)
            return self.api.check_image(frame_path).to_dataclass()

        if is_valid_image_path(snapshot):
            return self.api.check_image(snapshot).to_dataclass()

        raise MediaException("Expected snapshot to be image or video file, invalid format or file not found.", snapshot)

    def create_action_token(self, expires_in: Union[int, timedelta] = timedelta(hours=6), metadata: dict = {}) -> str:
        """
        Create a new action token
        """

        if isinstance(expires_in, timedelta):
            expires_in = expires_in.seconds

        token = self.api.create_action_token(expires_in, metadata)
        return token

