from __future__ import annotations
import dataclasses
import requests
from typing import Optional


@dataclasses.dataclass
class GetDocumentationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    