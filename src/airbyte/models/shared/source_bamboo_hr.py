from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceBambooHrBambooHrEnum(str, Enum):
    BAMBOO_HR = "bamboo-hr"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBambooHr:
    r"""SourceBambooHr
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceBambooHrBambooHrEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    custom_reports_fields: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports_fields'), 'exclude': lambda f: f is None }})
    custom_reports_include_default_fields: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports_include_default_fields'), 'exclude': lambda f: f is None }})
    