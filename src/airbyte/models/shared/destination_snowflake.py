from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationSnowflakeSnowflakeEnum(str, Enum):
    SNOWFLAKE = "snowflake"

class DestinationSnowflakeCredentialsUsernameAndPasswordAuthTypeEnum(str, Enum):
    USERNAME_AND_PASSWORD = "Username and Password"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCredentialsUsernameAndPassword:
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    auth_type: Optional[DestinationSnowflakeCredentialsUsernameAndPasswordAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    
class DestinationSnowflakeCredentialsKeyPairAuthenticationAuthTypeEnum(str, Enum):
    KEY_PAIR_AUTHENTICATION = "Key Pair Authentication"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCredentialsKeyPairAuthentication:
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key') }})
    auth_type: Optional[DestinationSnowflakeCredentialsKeyPairAuthenticationAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    private_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key_password'), 'exclude': lambda f: f is None }})
    
class DestinationSnowflakeCredentialsOAuth20AuthTypeEnum(str, Enum):
    O_AUTH2_0 = "OAuth2.0"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCredentialsOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    auth_type: Optional[DestinationSnowflakeCredentialsOAuth20AuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    
class DestinationSnowflakeLoadingMethodAzureBlobStorageStagingMethodEnum(str, Enum):
    AZURE_BLOB_STAGING = "Azure Blob Staging"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAzureBlobStorageStaging:
    r"""DestinationSnowflakeLoadingMethodAzureBlobStorageStaging
    Recommended for large production workloads for better speed and scalability.
    """
    
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    azure_blob_storage_container_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name') }})
    azure_blob_storage_sas_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_sas_token') }})
    method: DestinationSnowflakeLoadingMethodAzureBlobStorageStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    azure_blob_storage_endpoint_domain_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint_domain_name'), 'exclude': lambda f: f is None }})
    
class DestinationSnowflakeLoadingMethodGoogleCloudStorageStagingMethodEnum(str, Enum):
    GCS_STAGING = "GCS Staging"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodGoogleCloudStorageStaging:
    r"""DestinationSnowflakeLoadingMethodGoogleCloudStorageStaging
    Recommended for large production workloads for better speed and scalability.
    """
    
    bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket_name') }})
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    method: DestinationSnowflakeLoadingMethodGoogleCloudStorageStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryptionEncryptionTypeEnum(str, Enum):
    AES_CBC_ENVELOPE = "aes_cbc_envelope"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryption:
    r"""DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryption
    Staging data will be encrypted using AES-CBC envelope encryption.
    """
    
    encryption_type: DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryptionEncryptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type') }})
    key_encrypting_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key_encrypting_key'), 'exclude': lambda f: f is None }})
    
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionNoEncryptionEncryptionTypeEnum(str, Enum):
    NONE = "none"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionNoEncryption:
    r"""DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionNoEncryption
    Staging data will be stored in plaintext.
    """
    
    encryption_type: DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionNoEncryptionEncryptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type') }})
    
class DestinationSnowflakeLoadingMethodAWSS3StagingMethodEnum(str, Enum):
    S3_STAGING = "S3 Staging"

class DestinationSnowflakeLoadingMethodAWSS3StagingS3BucketRegionEnum(str, Enum):
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
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    EU_SOUTH_1 = "eu-south-1"
    EU_NORTH_1 = "eu-north-1"
    SA_EAST_1 = "sa-east-1"
    ME_SOUTH_1 = "me-south-1"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodAWSS3Staging:
    r"""DestinationSnowflakeLoadingMethodAWSS3Staging
    Recommended for large production workloads for better speed and scalability.
    """
    
    access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id') }})
    method: DestinationSnowflakeLoadingMethodAWSS3StagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key') }})
    encryption: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    purge_staging_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purge_staging_data'), 'exclude': lambda f: f is None }})
    s3_bucket_region: Optional[DestinationSnowflakeLoadingMethodAWSS3StagingS3BucketRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region'), 'exclude': lambda f: f is None }})
    
class DestinationSnowflakeLoadingMethodRecommendedInternalStagingMethodEnum(str, Enum):
    INTERNAL_STAGING = "Internal Staging"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodRecommendedInternalStaging:
    r"""DestinationSnowflakeLoadingMethodRecommendedInternalStaging
    Recommended for large production workloads for better speed and scalability.
    """
    
    method: DestinationSnowflakeLoadingMethodRecommendedInternalStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    
class DestinationSnowflakeLoadingMethodSelectAnotherOptionMethodEnum(str, Enum):
    STANDARD = "Standard"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeLoadingMethodSelectAnotherOption:
    r"""DestinationSnowflakeLoadingMethodSelectAnotherOption
    Select another option
    """
    
    method: DestinationSnowflakeLoadingMethodSelectAnotherOptionMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflake:
    r"""DestinationSnowflake
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationSnowflakeSnowflakeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    warehouse: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warehouse') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    loading_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loading_method'), 'exclude': lambda f: f is None }})
    