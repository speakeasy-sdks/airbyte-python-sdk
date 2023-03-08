import requests as requests_http
from . import utils
from airbyte.models import operations, shared
from typing import Optional

class Jobs:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def cancel_job(self, request: operations.CancelJobRequest) -> operations.CancelJobResponse:
        r"""Cancel a running Job
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/jobs/{jobId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CancelJobResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.JobResponse])
                res.job_response = out

        return res

    def create_job(self, request: operations.CreateJobRequest) -> operations.CreateJobResponse:
        r"""Trigger a sync or reset job of a connection
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/jobs'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateJobResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.JobResponse])
                res.job_response = out

        return res

    def get_job(self, request: operations.GetJobRequest) -> operations.GetJobResponse:
        r"""Get Job status and details
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/jobs/{jobId}', request.path_params)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetJobResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.JobResponse])
                res.job_response = out

        return res

    def list_jobs(self, request: operations.ListJobsRequest) -> operations.ListJobsResponse:
        r"""List Jobs by sync type
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/jobs'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListJobsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.JobsResponse])
                res.jobs_response = out

        return res

    