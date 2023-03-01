from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class GetDocumentationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    