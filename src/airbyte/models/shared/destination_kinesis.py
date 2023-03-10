from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class DestinationKinesisKinesisEnum(str, Enum):
    KINESIS = "kinesis"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationKinesis:
    r"""DestinationKinesis
    The values required to configure the destination.
    """
    
    access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessKey') }})
    airbyte_destination_name: DestinationKinesisKinesisEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    buffer_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bufferSize') }})
    endpoint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint') }})
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privateKey') }})
    region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    shard_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shardCount') }})
    