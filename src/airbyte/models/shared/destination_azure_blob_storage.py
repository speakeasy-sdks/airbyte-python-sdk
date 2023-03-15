from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationAzureBlobStorageAzureBlobStorageEnum(str, Enum):
    AZURE_BLOB_STORAGE = "azure-blob-storage"

class DestinationAzureBlobStorageFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum(str, Enum):
    JSONL = "JSONL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorageFormatJSONLinesNewlineDelimitedJSON:
    r"""DestinationAzureBlobStorageFormatJSONLinesNewlineDelimitedJSON
    Output data format
    """
    
    format_type: DestinationAzureBlobStorageFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    
class DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesNormalizationFlatteningEnum(str, Enum):
    NO_FLATTENING = "No flattening"
    ROOT_LEVEL_FLATTENING = "Root level flattening"

class DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesFormatTypeEnum(str, Enum):
    CSV = "CSV"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorageFormatCSVCommaSeparatedValues:
    r"""DestinationAzureBlobStorageFormatCSVCommaSeparatedValues
    Output data format
    """
    
    flattening: DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesNormalizationFlatteningEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening') }})
    format_type: DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorage:
    r"""DestinationAzureBlobStorage
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationAzureBlobStorageAzureBlobStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    azure_blob_storage_account_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_key') }})
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    format: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    azure_blob_storage_container_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name'), 'exclude': lambda f: f is None }})
    azure_blob_storage_endpoint_domain_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint_domain_name'), 'exclude': lambda f: f is None }})
    azure_blob_storage_output_buffer_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_output_buffer_size'), 'exclude': lambda f: f is None }})
    azure_blob_storage_spill_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_spill_size'), 'exclude': lambda f: f is None }})
    