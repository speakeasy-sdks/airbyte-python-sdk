from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceAmazonSqsAmazonSqsEnum(str, Enum):
    AMAZON_SQS = "amazon-sqs"

class SourceAmazonSqsAWSRegionEnum(str, Enum):
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    AF_SOUTH_1 = "af-south-1"
    AP_EAST_1 = "ap-east-1"
    AP_SOUTH_1 = "ap-south-1"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_NORTHEAST_3 = "ap-northeast-3"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    CA_CENTRAL_1 = "ca-central-1"
    CN_NORTH_1 = "cn-north-1"
    CN_NORTHWEST_1 = "cn-northwest-1"
    EU_CENTRAL_1 = "eu-central-1"
    EU_NORTH_1 = "eu-north-1"
    EU_SOUTH_1 = "eu-south-1"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    SA_EAST_1 = "sa-east-1"
    ME_SOUTH_1 = "me-south-1"
    US_GOV_EAST_1 = "us-gov-east-1"
    US_GOV_WEST_1 = "us-gov-west-1"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAmazonSqs:
    r"""SourceAmazonSqs
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceAmazonSqsAmazonSqsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    delete_messages: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_messages') }})
    queue_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queue_url') }})
    region: SourceAmazonSqsAWSRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key'), 'exclude': lambda f: f is None }})
    attributes_to_return: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes_to_return'), 'exclude': lambda f: f is None }})
    max_batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_batch_size'), 'exclude': lambda f: f is None }})
    max_wait_time: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_wait_time'), 'exclude': lambda f: f is None }})
    secret_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_key'), 'exclude': lambda f: f is None }})
    visibility_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visibility_timeout'), 'exclude': lambda f: f is None }})
    