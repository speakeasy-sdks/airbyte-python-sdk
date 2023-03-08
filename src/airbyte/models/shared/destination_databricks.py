from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationDatabricksDatabricksEnum(str, Enum):
    DATABRICKS = "databricks"

class DestinationDatabricksDataSourceAzureBlobStorageDataSourceTypeEnum(str, Enum):
    AZURE_BLOB_STORAGE = "Azure_Blob_Storage"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationDatabricksDataSourceAzureBlobStorage:
    r"""DestinationDatabricksDataSourceAzureBlobStorage
    Storage on which the delta lake is built.
    """
    
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    azure_blob_storage_container_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name') }})
    azure_blob_storage_sas_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_sas_token') }})
    data_source_type: DestinationDatabricksDataSourceAzureBlobStorageDataSourceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source_type') }})
    azure_blob_storage_endpoint_domain_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint_domain_name'), 'exclude': lambda f: f is None }})
    
class DestinationDatabricksDataSourceAmazonS3DataSourceTypeEnum(str, Enum):
    S3 = "S3"

class DestinationDatabricksDataSourceAmazonS3S3BucketRegionEnum(str, Enum):
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
class DestinationDatabricksDataSourceAmazonS3:
    r"""DestinationDatabricksDataSourceAmazonS3
    Storage on which the delta lake is built.
    """
    
    data_source_type: DestinationDatabricksDataSourceAmazonS3DataSourceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source_type') }})
    s3_access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_access_key_id') }})
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    s3_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path') }})
    s3_bucket_region: DestinationDatabricksDataSourceAmazonS3S3BucketRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region') }})
    s3_secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_secret_access_key') }})
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationDatabricks:
    r"""DestinationDatabricks
    The values required to configure the destination.
    """
    
    accept_terms: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accept_terms') }})
    airbyte_destination_name: DestinationDatabricksDatabricksEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    data_source: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source') }})
    databricks_http_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_http_path') }})
    databricks_personal_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_personal_access_token') }})
    databricks_server_hostname: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_server_hostname') }})
    database_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database_schema'), 'exclude': lambda f: f is None }})
    databricks_port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_port'), 'exclude': lambda f: f is None }})
    purge_staging_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purge_staging_data'), 'exclude': lambda f: f is None }})
    