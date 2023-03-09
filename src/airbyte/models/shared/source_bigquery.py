from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceBigqueryBigqueryEnum(str, Enum):
    BIGQUERY = "bigquery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBigquery:
    r"""SourceBigquery
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceBigqueryBigqueryEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    dataset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_id'), 'exclude': lambda f: f is None }})
    