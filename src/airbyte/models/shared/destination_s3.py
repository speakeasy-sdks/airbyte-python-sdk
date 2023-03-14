from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationS3S3Enum(str, Enum):
    S3 = "s3"

class DestinationS3FormatParquetColumnarStorageCompressionCodecEnum(str, Enum):
    UNCOMPRESSED = "UNCOMPRESSED"
    SNAPPY = "SNAPPY"
    GZIP = "GZIP"
    LZO = "LZO"
    BROTLI = "BROTLI"
    LZ4 = "LZ4"
    ZSTD = "ZSTD"

class DestinationS3FormatParquetColumnarStorageFormatTypeEnum(str, Enum):
    PARQUET = "Parquet"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatParquetColumnarStorage:
    r"""DestinationS3FormatParquetColumnarStorage
    Format of the data output. See <a href=\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\">here</a> for more details
    """
    
    format_type: DestinationS3FormatParquetColumnarStorageFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    block_size_mb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size_mb'), 'exclude': lambda f: f is None }})
    compression_codec: Optional[DestinationS3FormatParquetColumnarStorageCompressionCodecEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec'), 'exclude': lambda f: f is None }})
    dictionary_encoding: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_encoding'), 'exclude': lambda f: f is None }})
    dictionary_page_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_page_size_kb'), 'exclude': lambda f: f is None }})
    max_padding_size_mb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_padding_size_mb'), 'exclude': lambda f: f is None }})
    page_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size_kb'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum(str, Enum):
    GZIP = "GZIP"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionGZIP:
    r"""DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionGZIP
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".jsonl.gz\").
    """
    
    compression_type: Optional[DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum(str, Enum):
    NO_COMPRESSION = "No Compression"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionNoCompression:
    r"""DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionNoCompression
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".jsonl.gz\").
    """
    
    compression_type: Optional[DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatJSONLinesNewlineDelimitedJSONFlatteningEnum(str, Enum):
    NO_FLATTENING = "No flattening"
    ROOT_LEVEL_FLATTENING = "Root level flattening"

class DestinationS3FormatJSONLinesNewlineDelimitedJSONFormatTypeEnum(str, Enum):
    JSONL = "JSONL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatJSONLinesNewlineDelimitedJSON:
    r"""DestinationS3FormatJSONLinesNewlineDelimitedJSON
    Format of the data output. See <a href=\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\">here</a> for more details
    """
    
    format_type: DestinationS3FormatJSONLinesNewlineDelimitedJSONFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    flattening: Optional[DestinationS3FormatJSONLinesNewlineDelimitedJSONFlatteningEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatCSVCommaSeparatedValuesCompressionGZIPCompressionTypeEnum(str, Enum):
    GZIP = "GZIP"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatCSVCommaSeparatedValuesCompressionGZIP:
    r"""DestinationS3FormatCSVCommaSeparatedValuesCompressionGZIP
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".csv.gz\").
    """
    
    compression_type: Optional[DestinationS3FormatCSVCommaSeparatedValuesCompressionGZIPCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatCSVCommaSeparatedValuesCompressionNoCompressionCompressionTypeEnum(str, Enum):
    NO_COMPRESSION = "No Compression"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatCSVCommaSeparatedValuesCompressionNoCompression:
    r"""DestinationS3FormatCSVCommaSeparatedValuesCompressionNoCompression
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".csv.gz\").
    """
    
    compression_type: Optional[DestinationS3FormatCSVCommaSeparatedValuesCompressionNoCompressionCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatCSVCommaSeparatedValuesFlatteningEnum(str, Enum):
    NO_FLATTENING = "No flattening"
    ROOT_LEVEL_FLATTENING = "Root level flattening"

class DestinationS3FormatCSVCommaSeparatedValuesFormatTypeEnum(str, Enum):
    CSV = "CSV"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatCSVCommaSeparatedValues:
    r"""DestinationS3FormatCSVCommaSeparatedValues
    Format of the data output. See <a href=\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\">here</a> for more details
    """
    
    flattening: DestinationS3FormatCSVCommaSeparatedValuesFlatteningEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening') }})
    format_type: DestinationS3FormatCSVCommaSeparatedValuesFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatAvroApacheAvroCompressionCodecSnappyCodecEnum(str, Enum):
    SNAPPY = "snappy"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatAvroApacheAvroCompressionCodecSnappy:
    r"""DestinationS3FormatAvroApacheAvroCompressionCodecSnappy
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationS3FormatAvroApacheAvroCompressionCodecSnappyCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    
class DestinationS3FormatAvroApacheAvroCompressionCodecZstandardCodecEnum(str, Enum):
    ZSTANDARD = "zstandard"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatAvroApacheAvroCompressionCodecZstandard:
    r"""DestinationS3FormatAvroApacheAvroCompressionCodecZstandard
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationS3FormatAvroApacheAvroCompressionCodecZstandardCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    compression_level: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level') }})
    include_checksum: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_checksum'), 'exclude': lambda f: f is None }})
    
class DestinationS3FormatAvroApacheAvroCompressionCodecXzCodecEnum(str, Enum):
    XZ = "xz"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatAvroApacheAvroCompressionCodecXz:
    r"""DestinationS3FormatAvroApacheAvroCompressionCodecXz
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationS3FormatAvroApacheAvroCompressionCodecXzCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    compression_level: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level') }})
    
class DestinationS3FormatAvroApacheAvroCompressionCodecBzip2CodecEnum(str, Enum):
    BZIP2 = "bzip2"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatAvroApacheAvroCompressionCodecBzip2:
    r"""DestinationS3FormatAvroApacheAvroCompressionCodecBzip2
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationS3FormatAvroApacheAvroCompressionCodecBzip2CodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    
class DestinationS3FormatAvroApacheAvroCompressionCodecDeflateCodecEnum(str, Enum):
    DEFLATE = "Deflate"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatAvroApacheAvroCompressionCodecDeflate:
    r"""DestinationS3FormatAvroApacheAvroCompressionCodecDeflate
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationS3FormatAvroApacheAvroCompressionCodecDeflateCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    compression_level: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level') }})
    
class DestinationS3FormatAvroApacheAvroCompressionCodecNoCompressionCodecEnum(str, Enum):
    NO_COMPRESSION = "no compression"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatAvroApacheAvroCompressionCodecNoCompression:
    r"""DestinationS3FormatAvroApacheAvroCompressionCodecNoCompression
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationS3FormatAvroApacheAvroCompressionCodecNoCompressionCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    
class DestinationS3FormatAvroApacheAvroFormatTypeEnum(str, Enum):
    AVRO = "Avro"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3FormatAvroApacheAvro:
    r"""DestinationS3FormatAvroApacheAvro
    Format of the data output. See <a href=\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\">here</a> for more details
    """
    
    compression_codec: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec') }})
    format_type: DestinationS3FormatAvroApacheAvroFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    
class DestinationS3S3BucketRegionEnum(str, Enum):
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
class DestinationS3:
    r"""DestinationS3
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationS3S3Enum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    format: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    s3_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path') }})
    s3_bucket_region: DestinationS3S3BucketRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region') }})
    access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id'), 'exclude': lambda f: f is None }})
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    s3_endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_endpoint'), 'exclude': lambda f: f is None }})
    s3_path_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_path_format'), 'exclude': lambda f: f is None }})
    secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key'), 'exclude': lambda f: f is None }})
    