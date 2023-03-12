from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSalesforceSalesforceEnum(str, Enum):
    SALESFORCE = "salesforce"

class SourceSalesforceAuthTypeEnum(str, Enum):
    CLIENT = "Client"

class SourceSalesforceStreamsCriteriaSearchCriteriaEnum(str, Enum):
    STARTS_WITH = "starts with"
    ENDS_WITH = "ends with"
    CONTAINS = "contains"
    EXACTS = "exacts"
    STARTS_NOT_WITH = "starts not with"
    ENDS_NOT_WITH = "ends not with"
    NOT_CONTAINS = "not contains"
    NOT_EXACTS = "not exacts"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSalesforceStreamsCriteria:
    criteria: SourceSalesforceStreamsCriteriaSearchCriteriaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('criteria') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSalesforce:
    r"""SourceSalesforce
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceSalesforceSalesforceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    auth_type: Optional[SourceSalesforceAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    is_sandbox: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox'), 'exclude': lambda f: f is None }})
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    streams_criteria: Optional[list[SourceSalesforceStreamsCriteria]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streams_criteria'), 'exclude': lambda f: f is None }})
    