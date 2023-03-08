from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationS3GlueS3GlueEnum(str, Enum):
    S3_GLUE = "s3-glue"

class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum(str, Enum):
    GZIP = "GZIP"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionGZIP:
    r"""DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionGZIP
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".jsonl.gz\").
    """
    
    compression_type: Optional[DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum(str, Enum):
    NO_COMPRESSION = "No Compression"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionNoCompression:
    r"""DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionNoCompression
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".jsonl.gz\").
    """
    
    compression_type: Optional[DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum(str, Enum):
    JSONL = "JSONL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSON:
    r"""DestinationS3GlueFormatJSONLinesNewlineDelimitedJSON
    Format of the data output. See <a href=\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\">here</a> for more details
    """
    
    format_type: DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    flatten_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flatten_data'), 'exclude': lambda f: f is None }})
    
class DestinationS3GlueSerializationLibraryEnum(str, Enum):
    ORG_OPENX_DATA_JSONSERDE_JSON_SER_DE = "org.openx.data.jsonserde.JsonSerDe"
    ORG_APACHE_HIVE_HCATALOG_DATA_JSON_SER_DE = "org.apache.hive.hcatalog.data.JsonSerDe"

class DestinationS3GlueS3BucketRegionEnum(str, Enum):
    UNKNOWN = ""
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
class DestinationS3Glue:
    r"""DestinationS3Glue
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationS3GlueS3GlueEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    format: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    glue_database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('glue_database') }})
    glue_serialization_library: DestinationS3GlueSerializationLibraryEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('glue_serialization_library') }})
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    s3_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path') }})
    s3_bucket_region: DestinationS3GlueS3BucketRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region') }})
    access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id'), 'exclude': lambda f: f is None }})
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    s3_endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_endpoint'), 'exclude': lambda f: f is None }})
    s3_path_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_path_format'), 'exclude': lambda f: f is None }})
    secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key'), 'exclude': lambda f: f is None }})
    