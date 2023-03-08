from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationPubsubPubsubEnum(str, Enum):
    PUBSUB = "pubsub"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPubsub:
    r"""DestinationPubsub
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationPubsubPubsubEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    batching_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_enabled') }})
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    ordering_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ordering_enabled') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    topic_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_id') }})
    batching_delay_threshold: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_delay_threshold'), 'exclude': lambda f: f is None }})
    batching_element_count_threshold: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_element_count_threshold'), 'exclude': lambda f: f is None }})
    batching_request_bytes_threshold: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_request_bytes_threshold'), 'exclude': lambda f: f is None }})
    