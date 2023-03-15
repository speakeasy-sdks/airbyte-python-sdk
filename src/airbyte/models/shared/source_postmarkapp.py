from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourcePostmarkappPostmarkappEnum(str, Enum):
    POSTMARKAPP = "postmarkapp"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePostmarkapp:
    r"""SourcePostmarkapp
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePostmarkappPostmarkappEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    x_postmark_account_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('X-Postmark-Account-Token') }})
    x_postmark_server_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('X-Postmark-Server-Token') }})
    