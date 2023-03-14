from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import jobsresponse as shared_jobsresponse
from ..shared import jobtype_enum as shared_jobtype_enum
from typing import Optional


@dataclasses.dataclass
class ListJobsQueryParams:
    connection_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'connectionId', 'style': 'form', 'explode': True }})
    job_type: Optional[shared_jobtype_enum.JobTypeEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'jobType', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListJobsRequest:
    query_params: ListJobsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListJobsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    jobs_response: Optional[shared_jobsresponse.JobsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    