from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationFireboltFireboltEnum(str, Enum):
    FIREBOLT = "firebolt"

class DestinationFireboltLoadingMethodExternalTableViaS3MethodEnum(str, Enum):
    S3 = "S3"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationFireboltLoadingMethodExternalTableViaS3:
    r"""DestinationFireboltLoadingMethodExternalTableViaS3
    Loading method used to select the way data will be uploaded to Firebolt
    """
    
    aws_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_key_id') }})
    aws_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_key_secret') }})
    method: DestinationFireboltLoadingMethodExternalTableViaS3MethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    s3_bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket') }})
    s3_region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_region') }})
    
class DestinationFireboltLoadingMethodSQLInsertsMethodEnum(str, Enum):
    SQL = "SQL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationFireboltLoadingMethodSQLInserts:
    r"""DestinationFireboltLoadingMethodSQLInserts
    Loading method used to select the way data will be uploaded to Firebolt
    """
    
    method: DestinationFireboltLoadingMethodSQLInsertsMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationFirebolt:
    r"""DestinationFirebolt
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationFireboltFireboltEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    account: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account'), 'exclude': lambda f: f is None }})
    engine: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('engine'), 'exclude': lambda f: f is None }})
    host: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host'), 'exclude': lambda f: f is None }})
    loading_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loading_method'), 'exclude': lambda f: f is None }})
    