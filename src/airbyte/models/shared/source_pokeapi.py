from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourcePokeapiPokeapiEnum(str, Enum):
    POKEAPI = "pokeapi"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePokeapi:
    r"""SourcePokeapi
    The values required to configure the source.
    """
    
    airbyte_source_name: SourcePokeapiPokeapiEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    pokemon_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pokemon_name') }})
    