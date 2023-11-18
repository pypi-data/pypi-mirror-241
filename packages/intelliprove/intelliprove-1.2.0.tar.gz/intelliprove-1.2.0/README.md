<h1 align="center"> IntelliProve Python SDK</h1>

<div align="center">
    <img src="https://img.shields.io/pypi/dm/intelliprove" />
    <img src="https://img.shields.io/pypi/pyversions/intelliprove" />
    <img src="https://img.shields.io/pypi/v/intelliprove?label=version" />
</div>

# Requirements

- Python ^3.9

# Installation
```pip install intelliprove```

# Documentation

You can find our SDK documentation [here](https://docs.intelliprove.com/sdk-docs).

# Release Notes

- [1.2](#12)

## 1.2
### New features​

- Added `UnprocessableVideoResponse` model and `VideoProcessingFailedException` exception:
> The new model `UnprocessableVideoResponse` provides extra information about why a certain video did not successfully process. \
> This new information is returned inside the new `VideoProcessingFailedException` exception, which gets throw from the `get_results` method.
​
### Updates

- Refactor of `Quality` dataclass:
> The following properties for the `Quality` model have been renamed:
> - `message` => `prompt`
​
### ~~Deprecated features~~

### How to Upgrade

1. Ensure you are using the new property `prompt` from the `Quality` model
2. Ensure you catch the new `VideoProcessingFailedException` when calling the `get_results` method. Additionally you can read out the `response` property of this exception to provide feedback to the end-user.

<br>

## Example usage

```python
import os
from pathlib import Path

from intelliprove.api import IntelliproveApi, IntelliproveApiSettings, Biomarkers, Quality

# define api key and settings
apikey = os.environ.get('apikey')
settings = IntelliproveApiSettings(
    base_url=''
)

# init api
api = IntelliproveApi(apikey, settings)

# define the path of the video you want to upload
video_path = Path('./mydir/example.mp4')
image_path = Path('./mydir/example.png')

# manually check quality of a video of image
quality: Quality = api.check_conditions(video_path)
quality: Quality = api.check_conditions(image_path)

# Optional: define the performer and patient
performer: str = 'performer-a'
patient: str = 'patient-1'

# upload video to IntelliProve
# performer and patient are optional
uuid: str = api.upload(video_path)
# or
uuid: str = api.upload(video_path, performer=performer, patient=patient)

# get the results of the uploaded video
results: Biomarkers = api.get_results(uuid)
```

### Dataclasses
- Biomarkers
  - contains the results of an uploaded video
- Quality
  - contains the quality parameters of a video or image

### Exceptions
- ImageQualityException
- MediaException
- InvalidUuidException
- VideoProcessingFailedException
- ApiException
  - ApiNotFoundException
  - ApiForbiddenException
  - ApiErrorException
  - ApiResultNotAvailable
