from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class ResetConnectionPathParams:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResetConnectionRequest:
    path_params: ResetConnectionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ResetConnectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    