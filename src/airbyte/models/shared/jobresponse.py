from __future__ import annotations
import dataclasses
from ..shared import jobstatus_enum as shared_jobstatus_enum
from ..shared import jobtype_enum as shared_jobtype_enum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JobResponse:
    r"""JobResponse
    Provides details of a single job.
    """
    
    job_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobId') }})
    job_type: shared_jobtype_enum.JobTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobType') }})
    status: shared_jobstatus_enum.JobStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    