from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceS3S3Enum(str, Enum):
    S3 = "s3"

class SourceS3FormatJsonlFiletypeEnum(str, Enum):
    JSONL = "jsonl"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatJsonl:
    r"""SourceS3FormatJsonl
    This connector uses <a href=\"https://arrow.apache.org/docs/python/json.html\" target=\"_blank\">PyArrow</a> for JSON Lines (jsonl) file parsing.
    """
    
    block_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size'), 'exclude': lambda f: f is None }})
    filetype: Optional[SourceS3FormatJsonlFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    newlines_in_values: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newlines_in_values'), 'exclude': lambda f: f is None }})
    unexpected_field_behavior: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unexpected_field_behavior'), 'exclude': lambda f: f is None }})
    
class SourceS3FormatAvroFiletypeEnum(str, Enum):
    AVRO = "avro"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatAvro:
    r"""SourceS3FormatAvro
    This connector utilises <a href=\"https://fastavro.readthedocs.io/en/latest/\" target=\"_blank\">fastavro</a> for Avro parsing.
    """
    
    filetype: Optional[SourceS3FormatAvroFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    
class SourceS3FormatParquetFiletypeEnum(str, Enum):
    PARQUET = "parquet"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatParquet:
    r"""SourceS3FormatParquet
    This connector utilises <a href=\"https://arrow.apache.org/docs/python/generated/pyarrow.parquet.ParquetFile.html\" target=\"_blank\">PyArrow (Apache Arrow)</a> for Parquet parsing.
    """
    
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    buffer_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('buffer_size'), 'exclude': lambda f: f is None }})
    columns: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('columns'), 'exclude': lambda f: f is None }})
    filetype: Optional[SourceS3FormatParquetFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    
class SourceS3FormatCSVFiletypeEnum(str, Enum):
    CSV = "csv"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatCSV:
    r"""SourceS3FormatCSV
    This connector utilises <a href=\"https: // arrow.apache.org/docs/python/generated/pyarrow.csv.open_csv.html\" target=\"_blank\">PyArrow (Apache Arrow)</a> for CSV parsing.
    """
    
    additional_reader_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_reader_options'), 'exclude': lambda f: f is None }})
    advanced_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advanced_options'), 'exclude': lambda f: f is None }})
    block_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size'), 'exclude': lambda f: f is None }})
    delimiter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiter'), 'exclude': lambda f: f is None }})
    double_quote: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_quote'), 'exclude': lambda f: f is None }})
    encoding: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encoding'), 'exclude': lambda f: f is None }})
    escape_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escape_char'), 'exclude': lambda f: f is None }})
    filetype: Optional[SourceS3FormatCSVFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    infer_datatypes: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('infer_datatypes'), 'exclude': lambda f: f is None }})
    newlines_in_values: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newlines_in_values'), 'exclude': lambda f: f is None }})
    quote_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quote_char'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3S3AmazonWebServices:
    r"""SourceS3S3AmazonWebServices
    Use this to load files from S3 or S3-compatible services
    """
    
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    aws_access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id'), 'exclude': lambda f: f is None }})
    aws_secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key'), 'exclude': lambda f: f is None }})
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    path_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path_prefix'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3:
    r"""SourceS3
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceS3S3Enum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    dataset: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset') }})
    path_pattern: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path_pattern') }})
    provider: SourceS3S3AmazonWebServices = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    format: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    