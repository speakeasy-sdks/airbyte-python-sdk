from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields

class SourceAwsCloudtrailAwsCloudtrailEnum(str, Enum):
    AWS_CLOUDTRAIL = "aws-cloudtrail"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAwsCloudtrail:
    r"""SourceAwsCloudtrail
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceAwsCloudtrailAwsCloudtrailEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    aws_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_key_id') }})
    aws_region_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_region_name') }})
    aws_secret_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_key') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    