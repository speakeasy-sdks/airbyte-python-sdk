from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import jobcreate as shared_jobcreate
from ..shared import jobresponse as shared_jobresponse
from typing import Optional


@dataclasses.dataclass
class CreateJobRequest:
    request: shared_jobcreate.JobCreate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    job_response: Optional[shared_jobresponse.JobResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    