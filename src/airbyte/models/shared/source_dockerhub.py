from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceDockerhubDockerhubEnum(str, Enum):
    DOCKERHUB = "dockerhub"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDockerhub:
    r"""SourceDockerhub
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceDockerhubDockerhubEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    docker_username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('docker_username') }})
    