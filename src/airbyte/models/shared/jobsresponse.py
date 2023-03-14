from __future__ import annotations
import dataclasses
from ..shared import jobresponse as shared_jobresponse
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JobsResponse:
    data: list[shared_jobresponse.JobResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    next: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next') }})
    previous: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous') }})
    