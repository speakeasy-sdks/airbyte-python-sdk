from __future__ import annotations
import dataclasses
from ..shared import jobtype_enum as shared_jobtype_enum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JobCreate:
    r"""JobCreate
    Creates a new Job from the configuration provided in the request body
    """
    
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId') }})
    job_type: shared_jobtype_enum.JobTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobType') }})
    