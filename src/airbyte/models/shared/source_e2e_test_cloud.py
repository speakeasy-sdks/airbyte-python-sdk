from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceE2eTestCloudE2eTestCloudEnum(str, Enum):
    E2E_TEST_CLOUD = "e2e-test-cloud"

class SourceE2eTestCloudMockCatalogMultiSchemaTypeEnum(str, Enum):
    MULTI_STREAM = "MULTI_STREAM"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceE2eTestCloudMockCatalogMultiSchema:
    r"""SourceE2eTestCloudMockCatalogMultiSchema
    A catalog with multiple data streams, each with a different schema.
    """
    
    stream_schemas: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schemas') }})
    type: SourceE2eTestCloudMockCatalogMultiSchemaTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    
class SourceE2eTestCloudMockCatalogSingleSchemaTypeEnum(str, Enum):
    SINGLE_STREAM = "SINGLE_STREAM"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceE2eTestCloudMockCatalogSingleSchema:
    r"""SourceE2eTestCloudMockCatalogSingleSchema
    A catalog with one or multiple streams that share the same schema.
    """
    
    stream_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_name') }})
    stream_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schema') }})
    type: SourceE2eTestCloudMockCatalogSingleSchemaTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    stream_duplication: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_duplication'), 'exclude': lambda f: f is None }})
    
class SourceE2eTestCloudTypeEnum(str, Enum):
    CONTINUOUS_FEED = "CONTINUOUS_FEED"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceE2eTestCloud:
    r"""SourceE2eTestCloud
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceE2eTestCloudE2eTestCloudEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    max_messages: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_messages') }})
    mock_catalog: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mock_catalog') }})
    message_interval_ms: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_interval_ms'), 'exclude': lambda f: f is None }})
    seed: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    type: Optional[SourceE2eTestCloudTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    