from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationcreate as shared_destinationcreate
from ..shared import destinationid as shared_destinationid
from typing import Optional


@dataclasses.dataclass
class CreateDestinationRequest:
    request: Optional[shared_destinationcreate.DestinationCreate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateDestinationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    destination_id: Optional[shared_destinationid.DestinationID] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    