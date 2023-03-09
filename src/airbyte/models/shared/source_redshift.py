from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceRedshiftRedshiftEnum(str, Enum):
    REDSHIFT = "redshift"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRedshift:
    r"""SourceRedshift
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceRedshiftRedshiftEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    schemas: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    