from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSftpBulkSftpBulkEnum(str, Enum):
    SFTP_BULK = "sftp-bulk"

class SourceSftpBulkFileTypeEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulk:
    r"""SourceSftpBulk
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSftpBulkSftpBulkEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    folder_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_path') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    stream_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_name') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    file_most_recent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_most_recent'), 'exclude': lambda f: f is None }})
    file_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_pattern'), 'exclude': lambda f: f is None }})
    file_type: Optional[SourceSftpBulkFileTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_type'), 'exclude': lambda f: f is None }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    private_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key'), 'exclude': lambda f: f is None }})
    