from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceMailjetSmsMailjetSmsEnum(str, Enum):
    MAILJET_SMS = "mailjet-sms"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailjetSms:
    r"""SourceMailjetSms
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceMailjetSmsMailjetSmsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    end_date: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    start_date: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    