from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationGcsGcsEnum(str, Enum):
    GCS = "gcs"

class DestinationGcsCredentialHMACKeyCredentialTypeEnum(str, Enum):
    HMAC_KEY = "HMAC_KEY"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsCredentialHMACKey:
    r"""DestinationGcsCredentialHMACKey
    An HMAC key is a type of credential and can be associated with a service account or a user account in Cloud Storage. Read more <a href=\"https://cloud.google.com/storage/docs/authentication/hmackeys\">here</a>.
    """
    
    credential_type: DestinationGcsCredentialHMACKeyCredentialTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential_type') }})
    hmac_key_access_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_access_id') }})
    hmac_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_secret') }})
    
class DestinationGcsFormatParquetColumnarStorageCompressionCodecEnum(str, Enum):
    UNCOMPRESSED = "UNCOMPRESSED"
    SNAPPY = "SNAPPY"
    GZIP = "GZIP"
    LZO = "LZO"
    BROTLI = "BROTLI"
    LZ4 = "LZ4"
    ZSTD = "ZSTD"

class DestinationGcsFormatParquetColumnarStorageFormatTypeEnum(str, Enum):
    PARQUET = "Parquet"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatParquetColumnarStorage:
    r"""DestinationGcsFormatParquetColumnarStorage
    Output data format. One of the following formats must be selected - <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro\">AVRO</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas\">PARQUET</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table\">CSV</a> format, or <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table\">JSONL</a> format.
    """
    
    format_type: DestinationGcsFormatParquetColumnarStorageFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    block_size_mb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size_mb'), 'exclude': lambda f: f is None }})
    compression_codec: Optional[DestinationGcsFormatParquetColumnarStorageCompressionCodecEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec'), 'exclude': lambda f: f is None }})
    dictionary_encoding: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_encoding'), 'exclude': lambda f: f is None }})
    dictionary_page_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_page_size_kb'), 'exclude': lambda f: f is None }})
    max_padding_size_mb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_padding_size_mb'), 'exclude': lambda f: f is None }})
    page_size_kb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size_kb'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum(str, Enum):
    GZIP = "GZIP"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionGZIP:
    r"""DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionGZIP
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".jsonl.gz\").
    """
    
    compression_type: Optional[DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum(str, Enum):
    NO_COMPRESSION = "No Compression"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionNoCompression:
    r"""DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionNoCompression
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".jsonl.gz\").
    """
    
    compression_type: Optional[DestinationGcsFormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum(str, Enum):
    JSONL = "JSONL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatJSONLinesNewlineDelimitedJSON:
    r"""DestinationGcsFormatJSONLinesNewlineDelimitedJSON
    Output data format. One of the following formats must be selected - <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro\">AVRO</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas\">PARQUET</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table\">CSV</a> format, or <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table\">JSONL</a> format.
    """
    
    format_type: DestinationGcsFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatCSVCommaSeparatedValuesCompressionGZIPCompressionTypeEnum(str, Enum):
    GZIP = "GZIP"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatCSVCommaSeparatedValuesCompressionGZIP:
    r"""DestinationGcsFormatCSVCommaSeparatedValuesCompressionGZIP
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".csv.gz\").
    """
    
    compression_type: Optional[DestinationGcsFormatCSVCommaSeparatedValuesCompressionGZIPCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatCSVCommaSeparatedValuesCompressionNoCompressionCompressionTypeEnum(str, Enum):
    NO_COMPRESSION = "No Compression"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatCSVCommaSeparatedValuesCompressionNoCompression:
    r"""DestinationGcsFormatCSVCommaSeparatedValuesCompressionNoCompression
    Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \".csv.gz\").
    """
    
    compression_type: Optional[DestinationGcsFormatCSVCommaSeparatedValuesCompressionNoCompressionCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatCSVCommaSeparatedValuesNormalizationEnum(str, Enum):
    NO_FLATTENING = "No flattening"
    ROOT_LEVEL_FLATTENING = "Root level flattening"

class DestinationGcsFormatCSVCommaSeparatedValuesFormatTypeEnum(str, Enum):
    CSV = "CSV"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatCSVCommaSeparatedValues:
    r"""DestinationGcsFormatCSVCommaSeparatedValues
    Output data format. One of the following formats must be selected - <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro\">AVRO</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas\">PARQUET</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table\">CSV</a> format, or <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table\">JSONL</a> format.
    """
    
    format_type: DestinationGcsFormatCSVCommaSeparatedValuesFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    flattening: Optional[DestinationGcsFormatCSVCommaSeparatedValuesNormalizationEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatAvroApacheAvroCompressionCodecSnappyCodecEnum(str, Enum):
    SNAPPY = "snappy"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatAvroApacheAvroCompressionCodecSnappy:
    r"""DestinationGcsFormatAvroApacheAvroCompressionCodecSnappy
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationGcsFormatAvroApacheAvroCompressionCodecSnappyCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    
class DestinationGcsFormatAvroApacheAvroCompressionCodecZstandardCodecEnum(str, Enum):
    ZSTANDARD = "zstandard"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatAvroApacheAvroCompressionCodecZstandard:
    r"""DestinationGcsFormatAvroApacheAvroCompressionCodecZstandard
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationGcsFormatAvroApacheAvroCompressionCodecZstandardCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    compression_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    include_checksum: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_checksum'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatAvroApacheAvroCompressionCodecXzCodecEnum(str, Enum):
    XZ = "xz"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatAvroApacheAvroCompressionCodecXz:
    r"""DestinationGcsFormatAvroApacheAvroCompressionCodecXz
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationGcsFormatAvroApacheAvroCompressionCodecXzCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    compression_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatAvroApacheAvroCompressionCodecBzip2CodecEnum(str, Enum):
    BZIP2 = "bzip2"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatAvroApacheAvroCompressionCodecBzip2:
    r"""DestinationGcsFormatAvroApacheAvroCompressionCodecBzip2
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationGcsFormatAvroApacheAvroCompressionCodecBzip2CodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    
class DestinationGcsFormatAvroApacheAvroCompressionCodecDeflateCodecEnum(str, Enum):
    DEFLATE = "Deflate"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatAvroApacheAvroCompressionCodecDeflate:
    r"""DestinationGcsFormatAvroApacheAvroCompressionCodecDeflate
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationGcsFormatAvroApacheAvroCompressionCodecDeflateCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    compression_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    
class DestinationGcsFormatAvroApacheAvroCompressionCodecNoCompressionCodecEnum(str, Enum):
    NO_COMPRESSION = "no compression"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatAvroApacheAvroCompressionCodecNoCompression:
    r"""DestinationGcsFormatAvroApacheAvroCompressionCodecNoCompression
    The compression algorithm used to compress data. Default to no compression.
    """
    
    codec: DestinationGcsFormatAvroApacheAvroCompressionCodecNoCompressionCodecEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec') }})
    
class DestinationGcsFormatAvroApacheAvroFormatTypeEnum(str, Enum):
    AVRO = "Avro"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsFormatAvroApacheAvro:
    r"""DestinationGcsFormatAvroApacheAvro
    Output data format. One of the following formats must be selected - <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro\">AVRO</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas\">PARQUET</a> format, <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table\">CSV</a> format, or <a href=\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table\">JSONL</a> format.
    """
    
    compression_codec: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec') }})
    format_type: DestinationGcsFormatAvroApacheAvroFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    
class DestinationGCSGCSBucketRegionEnum(str, Enum):
    NORTHAMERICA_NORTHEAST1 = "northamerica-northeast1"
    NORTHAMERICA_NORTHEAST2 = "northamerica-northeast2"
    US_CENTRAL1 = "us-central1"
    US_EAST1 = "us-east1"
    US_EAST4 = "us-east4"
    US_WEST1 = "us-west1"
    US_WEST2 = "us-west2"
    US_WEST3 = "us-west3"
    US_WEST4 = "us-west4"
    SOUTHAMERICA_EAST1 = "southamerica-east1"
    SOUTHAMERICA_WEST1 = "southamerica-west1"
    EUROPE_CENTRAL2 = "europe-central2"
    EUROPE_NORTH1 = "europe-north1"
    EUROPE_WEST1 = "europe-west1"
    EUROPE_WEST2 = "europe-west2"
    EUROPE_WEST3 = "europe-west3"
    EUROPE_WEST4 = "europe-west4"
    EUROPE_WEST6 = "europe-west6"
    ASIA_EAST1 = "asia-east1"
    ASIA_EAST2 = "asia-east2"
    ASIA_NORTHEAST1 = "asia-northeast1"
    ASIA_NORTHEAST2 = "asia-northeast2"
    ASIA_NORTHEAST3 = "asia-northeast3"
    ASIA_SOUTH1 = "asia-south1"
    ASIA_SOUTH2 = "asia-south2"
    ASIA_SOUTHEAST1 = "asia-southeast1"
    ASIA_SOUTHEAST2 = "asia-southeast2"
    AUSTRALIA_SOUTHEAST1 = "australia-southeast1"
    AUSTRALIA_SOUTHEAST2 = "australia-southeast2"
    ASIA = "asia"
    EU = "eu"
    US = "us"
    ASIA1 = "asia1"
    EUR4 = "eur4"
    NAM4 = "nam4"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcs:
    r"""DestinationGcs
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationGcsGcsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    credential: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential') }})
    format: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    gcs_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_name') }})
    gcs_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_path') }})
    gcs_bucket_region: Optional[DestinationGCSGCSBucketRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_region'), 'exclude': lambda f: f is None }})
    