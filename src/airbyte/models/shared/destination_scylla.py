from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationScyllaScyllaEnum(str, Enum):
    SCYLLA = "scylla"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationScylla:
    r"""DestinationScylla
    The values required to configure the destination.
    """
    
    address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    airbyte_destination_name: DestinationScyllaScyllaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    keyspace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keyspace') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    replication: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication'), 'exclude': lambda f: f is None }})
    