from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class SyncConnectionPathParams:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SyncConnectionRequest:
    path_params: SyncConnectionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class SyncConnectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    