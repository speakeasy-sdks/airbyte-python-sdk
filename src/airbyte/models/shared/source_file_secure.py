from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceFileSecureFileSecureEnum(str, Enum):
    FILE_SECURE = "file-secure"

class SourceFileSecureFileFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"
    JSONL = "jsonl"
    EXCEL = "excel"
    EXCEL_BINARY = "excel_binary"
    FEATHER = "feather"
    PARQUET = "parquet"
    YAML = "yaml"

class SourceFileSecureProviderSFTPSecureFileTransferProtocolStorageEnum(str, Enum):
    SFTP = "SFTP"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderSFTPSecureFileTransferProtocol:
    r"""SourceFileSecureProviderSFTPSecureFileTransferProtocol
    The storage Provider or Location of the file(s) which should be replicated.
    """
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    storage: SourceFileSecureProviderSFTPSecureFileTransferProtocolStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderSCPSecureCopyProtocolStorageEnum(str, Enum):
    SCP = "SCP"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderSCPSecureCopyProtocol:
    r"""SourceFileSecureProviderSCPSecureCopyProtocol
    The storage Provider or Location of the file(s) which should be replicated.
    """
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    storage: SourceFileSecureProviderSCPSecureCopyProtocolStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderSSHSecureShellStorageEnum(str, Enum):
    SSH = "SSH"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderSSHSecureShell:
    r"""SourceFileSecureProviderSSHSecureShell
    The storage Provider or Location of the file(s) which should be replicated.
    """
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    storage: SourceFileSecureProviderSSHSecureShellStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderAzBlobAzureBlobStorageStorageEnum(str, Enum):
    AZ_BLOB = "AzBlob"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderAzBlobAzureBlobStorage:
    r"""SourceFileSecureProviderAzBlobAzureBlobStorage
    The storage Provider or Location of the file(s) which should be replicated.
    """
    
    storage: SourceFileSecureProviderAzBlobAzureBlobStorageStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    storage_account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_account') }})
    sas_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas_token'), 'exclude': lambda f: f is None }})
    shared_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shared_key'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderS3AmazonWebServicesStorageEnum(str, Enum):
    S3 = "S3"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderS3AmazonWebServices:
    r"""SourceFileSecureProviderS3AmazonWebServices
    The storage Provider or Location of the file(s) which should be replicated.
    """
    
    storage: SourceFileSecureProviderS3AmazonWebServicesStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    aws_access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id'), 'exclude': lambda f: f is None }})
    aws_secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderGCSGoogleCloudStorageStorageEnum(str, Enum):
    GCS = "GCS"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderGCSGoogleCloudStorage:
    r"""SourceFileSecureProviderGCSGoogleCloudStorage
    The storage Provider or Location of the file(s) which should be replicated.
    """
    
    storage: SourceFileSecureProviderGCSGoogleCloudStorageStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    service_account_json: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_json'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderHTTPSPublicWebStorageEnum(str, Enum):
    HTTPS = "HTTPS"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderHTTPSPublicWeb:
    r"""SourceFileSecureProviderHTTPSPublicWeb
    The storage Provider or Location of the file(s) which should be replicated.
    """
    
    storage: SourceFileSecureProviderHTTPSPublicWebStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user_agent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_agent'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecure:
    r"""SourceFileSecure
    The values required to configure the source.
    """
    
    airbyte_source_name: SourceFileSecureFileSecureEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-source-name') }})
    dataset_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_name') }})
    format: SourceFileSecureFileFormatEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    provider: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    reader_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reader_options'), 'exclude': lambda f: f is None }})
    