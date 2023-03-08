from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceBraintreeBraintreeEnum(str, Enum):
    BRAINTREE = "braintree"

class SourceBraintreeEnvironmentEnum(str, Enum):
    DEVELOPMENT = "Development"
    SANDBOX = "Sandbox"
    QA = "Qa"
    PRODUCTION = "Production"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBraintree:
    r"""SourceBraintree
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceBraintreeBraintreeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    environment: SourceBraintreeEnvironmentEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment') }})
    merchant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_id') }})
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key') }})
    public_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public_key') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    