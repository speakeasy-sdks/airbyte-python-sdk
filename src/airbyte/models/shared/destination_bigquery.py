from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationBigqueryBigqueryEnum(str, Enum):
    BIGQUERY = "bigquery"

class DestinationBigqueryDatasetLocationEnum(str, Enum):
    US = "US"
    EU = "EU"
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
    EUROPE_CENTRAL2 = "europe-central2"
    EUROPE_NORTH1 = "europe-north1"
    EUROPE_WEST1 = "europe-west1"
    EUROPE_WEST2 = "europe-west2"
    EUROPE_WEST3 = "europe-west3"
    EUROPE_WEST4 = "europe-west4"
    EUROPE_WEST6 = "europe-west6"
    NORTHAMERICA_NORTHEAST1 = "northamerica-northeast1"
    NORTHAMERICA_NORTHEAST2 = "northamerica-northeast2"
    SOUTHAMERICA_EAST1 = "southamerica-east1"
    SOUTHAMERICA_WEST1 = "southamerica-west1"
    US_CENTRAL1 = "us-central1"
    US_EAST1 = "us-east1"
    US_EAST4 = "us-east4"
    US_WEST1 = "us-west1"
    US_WEST2 = "us-west2"
    US_WEST3 = "us-west3"
    US_WEST4 = "us-west4"

class DestinationBigqueryLoadingMethodGCSStagingCredentialHMACKeyCredentialTypeEnum(str, Enum):
    HMAC_KEY = "HMAC_KEY"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigqueryLoadingMethodGCSStagingCredentialHMACKey:
    r"""DestinationBigqueryLoadingMethodGCSStagingCredentialHMACKey
    An HMAC key is a type of credential and can be associated with a service account or a user account in Cloud Storage. Read more <a href=\"https://cloud.google.com/storage/docs/authentication/hmackeys\">here</a>.
    """
    
    credential_type: DestinationBigqueryLoadingMethodGCSStagingCredentialHMACKeyCredentialTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential_type') }})
    hmac_key_access_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_access_id') }})
    hmac_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_secret') }})
    
class DestinationBigqueryLoadingMethodGCSStagingGCSTmpFilesAfterwardProcessingEnum(str, Enum):
    DELETE_ALL_TMP_FILES_FROM_GCS = "Delete all tmp files from GCS"
    KEEP_ALL_TMP_FILES_IN_GCS = "Keep all tmp files in GCS"

class DestinationBigqueryLoadingMethodGCSStagingMethodEnum(str, Enum):
    GCS_STAGING = "GCS Staging"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigqueryLoadingMethodGCSStaging:
    r"""DestinationBigqueryLoadingMethodGCSStaging
    Loading method used to send select the way data will be uploaded to BigQuery. <br/><b>Standard Inserts</b> - Direct uploading using SQL INSERT statements. This method is extremely inefficient and provided only for quick testing. In almost all cases, you should use staging. <br/><b>GCS Staging</b> - Writes large batches of records to a file, uploads the file to GCS, then uses <b>COPY INTO table</b> to upload the file. Recommended for most workloads for better speed and scalability. Read more about GCS Staging <a href=\"https://docs.airbyte.com/integrations/destinations/bigquery#gcs-staging\">here</a>.
    """
    
    credential: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential') }})
    gcs_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_name') }})
    gcs_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_path') }})
    method: DestinationBigqueryLoadingMethodGCSStagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    keep_files_in_gcs_bucket: Optional[DestinationBigqueryLoadingMethodGCSStagingGCSTmpFilesAfterwardProcessingEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keep_files_in_gcs-bucket'), 'exclude': lambda f: f is None }})
    
class DestinationBigqueryLoadingMethodStandardInsertsMethodEnum(str, Enum):
    STANDARD = "Standard"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigqueryLoadingMethodStandardInserts:
    r"""DestinationBigqueryLoadingMethodStandardInserts
    Loading method used to send select the way data will be uploaded to BigQuery. <br/><b>Standard Inserts</b> - Direct uploading using SQL INSERT statements. This method is extremely inefficient and provided only for quick testing. In almost all cases, you should use staging. <br/><b>GCS Staging</b> - Writes large batches of records to a file, uploads the file to GCS, then uses <b>COPY INTO table</b> to upload the file. Recommended for most workloads for better speed and scalability. Read more about GCS Staging <a href=\"https://docs.airbyte.com/integrations/destinations/bigquery#gcs-staging\">here</a>.
    """
    
    method: DestinationBigqueryLoadingMethodStandardInsertsMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    
class DestinationBigqueryTransformationQueryRunTypeEnum(str, Enum):
    INTERACTIVE = "interactive"
    BATCH = "batch"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationBigquery:
    r"""DestinationBigquery
    The values required to configure the destination.
    """
    
    airbyte_destination_name: DestinationBigqueryBigqueryEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('airbyte-destination-name') }})
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_id') }})
    dataset_location: DestinationBigqueryDatasetLocationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_location') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    big_query_client_buffer_size_mb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('big_query_client_buffer_size_mb'), 'exclude': lambda f: f is None }})
    credentials_json: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json'), 'exclude': lambda f: f is None }})
    loading_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loading_method'), 'exclude': lambda f: f is None }})
    transformation_priority: Optional[DestinationBigqueryTransformationQueryRunTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transformation_priority'), 'exclude': lambda f: f is None }})
    