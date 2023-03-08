from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourcePipedrivePipedriveEnum(str, Enum):
    PIPEDRIVE = "pipedrive"

class SourcePipedriveAPIKeyAuthenticationAuthTypeEnum(str, Enum):
    TOKEN = "Token"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePipedriveAPIKeyAuthentication:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    auth_type: SourcePipedriveAPIKeyAuthenticationAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePipedrive:
    r"""SourcePipedrive
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePipedrivePipedriveEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    replication_start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    authorization: Optional[SourcePipedriveAPIKeyAuthentication] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization'), 'exclude': lambda f: f is None }})
    