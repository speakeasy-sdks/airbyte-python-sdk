from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationPulsarPulsarEnum(str, Enum):
    PULSAR = "pulsar"

class DestinationPulsarCompressionTypeEnum(str, Enum):
    NONE = "NONE"
    LZ4 = "LZ4"
    ZLIB = "ZLIB"
    ZSTD = "ZSTD"
    SNAPPY = "SNAPPY"

class DestinationPulsarTopicTypeEnum(str, Enum):
    PERSISTENT = "persistent"
    NON_PERSISTENT = "non-persistent"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPulsar:
    r"""DestinationPulsar
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationPulsarPulsarEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    batching_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_enabled') }})
    batching_max_messages: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_max_messages') }})
    batching_max_publish_delay: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_max_publish_delay') }})
    block_if_queue_full: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_if_queue_full') }})
    brokers: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brokers') }})
    compression_type: DestinationPulsarCompressionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type') }})
    max_pending_messages: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_pending_messages') }})
    max_pending_messages_across_partitions: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_pending_messages_across_partitions') }})
    send_timeout_ms: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('send_timeout_ms') }})
    topic_namespace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_namespace') }})
    topic_pattern: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_pattern') }})
    topic_tenant: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_tenant') }})
    topic_type: DestinationPulsarTopicTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_type') }})
    use_tls: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('use_tls') }})
    producer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('producer_name'), 'exclude': lambda f: f is None }})
    producer_sync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('producer_sync'), 'exclude': lambda f: f is None }})
    topic_test: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_test'), 'exclude': lambda f: f is None }})
    