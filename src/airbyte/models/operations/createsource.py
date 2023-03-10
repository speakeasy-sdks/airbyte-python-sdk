from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import sourcecreate as shared_sourcecreate
from ..shared import sourceid as shared_sourceid
from typing import Optional


@dataclasses.dataclass
class CreateSourceRequest:
    request: Optional[shared_sourcecreate.SourceCreate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    source_id: Optional[shared_sourceid.SourceID] = dataclasses.field(default=None)
    