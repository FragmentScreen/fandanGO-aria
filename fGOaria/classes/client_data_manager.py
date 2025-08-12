from typing import Union, Dict, Any
from dotenv import load_dotenv
from fGOaria.classes.field import Field
from fGOaria.classes.bucket import Bucket
from fGOaria.classes.record import Record
from fGOaria.classes.aria_client import AriaClient
from fGOaria.utils.imports_config import *
from fGOaria.utils.queries import (
    CREATE_DATA_BUCKET, CREATE_DATA_RECORD, CREATE_DATA_FIELD,
    BUCKET_ITEMS, RECORD_ITEMS, FIELD_ITEMS
)

load_dotenv()

class DataManagerClient(AriaClient):
    def __init__(self, token: str, entity_id: int, entity_type: str):
        super().__init__(token)
        self.id = entity_id
        self.type = entity_type

    # BUCKETS
    def push_bucket(self, bucket: Bucket) -> Union[Dict[str, Any], None]:
        """Create a new data bucket."""
        variables = {
            "input": {
                "aria_id": bucket.entity_id,
                "aria_entity_type": bucket.entity_type,
                "embargoed_until": bucket.embargo_date
            }
        }
        response = self.gql_query(CREATE_DATA_BUCKET.query, variables)
        return response['data'][CREATE_DATA_BUCKET.return_key]

    def pull_buckets(self, id: int, type: str) -> Union[Dict[str, Any], None]:
        """Pull data buckets from database based on aria id & entity."""
        variables = {
            "filters": {
                "aria_id": id,
                "aria_entity_type": type
            }
        }
        response = self.gql_query(BUCKET_ITEMS.query, variables)
        return response['data'][BUCKET_ITEMS.return_key]

    # RECORDS
    def push_record(self, record: Record) -> Union[Dict[str, Any], None]:
        """Create a new data record."""
        variables = {
            "input": {
                "bucket": record.bucket_id,
                "schema": record.schema_type
            }
        }
        response = self.gql_query(CREATE_DATA_RECORD.query, variables)
        return response['data'][CREATE_DATA_RECORD.return_key]

    def pull_records(self, bucket_id: str) -> Union[Dict[str, Any], None]:
        """Pull data records from database based on Bucket ID."""
        variables = {
            "filters": {
                "bucket": bucket_id
            }
        }
        response = self.gql_query(RECORD_ITEMS.query, variables)
        return response['data'][RECORD_ITEMS.return_key]

    # FIELDS
    def push_field(self, field: Field) -> Union[Dict[str, Any], None]:
        """Create a new data field."""
        field.content = json.dumps(field.content)
        variables = {
            "input": {
                "record": field.record_id,
                "type": field.field_type,
                "content": field.content,
                "options": field.options
            }
        }
        response = self.gql_query(CREATE_DATA_FIELD.query, variables)
        return response['data'][CREATE_DATA_FIELD.return_key]

    def pull_fields(self, record_id: str) -> Union[Dict[str, Any], None]:
        """Pull data fields from database based on Record ID."""
        variables = {
            "filters": {
                "record": record_id
            }
        }
        response = self.gql_query(FIELD_ITEMS.query, variables)
        return response['data'][FIELD_ITEMS.return_key]
