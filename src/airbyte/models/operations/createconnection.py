from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectionid as shared_connectionid
from typing import Optional


@dataclasses.dataclass
class CreateConnectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connection_id: Optional[shared_connectionid.ConnectionID] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    