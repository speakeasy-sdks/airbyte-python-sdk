from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceZendeskSupportZendeskSupportEnum(str, Enum):
    ZENDESK_SUPPORT = "zendesk-support"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskSupport:
    r"""SourceZendeskSupport
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceZendeskSupportZendeskSupportEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    ignore_pagination: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ignore_pagination'), 'exclude': lambda f: f is None }})
    