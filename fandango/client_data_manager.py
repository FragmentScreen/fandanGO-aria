import requests
from .api_client import APIClient
from .config import *
from .utils import set_headers, pretty_print

class DataManagerClient(APIClient):
    def __init__(self, token, entity_id, entity_type):
        super().__init__(token)
        self.token = token
        self.create_bucket_url = 'createDataBucket'
        self.create_record_url = 'createDataRecord'
        self.create_field_url = 'createDataField'
        self.id = entity_id
        self.type = entity_type

    def push_bucket(self, bucket) -> dict | None :
        data = {
            'aria_id': bucket.entity_id,
            "aria_entity_type" : bucket.entity_type, 
            'embargoed_until' : bucket.embargo_date
        }
        response = self.post(self.create_bucket_url, data)
        bucket = response['data']['items'][0]
        return bucket
    
    def push_record(self, record) -> dict or None :
        data = {
            "bucket" : record.bucket_id,
            "schema" : record.schema_type
        }
        response = self.post(self.create_record_url, data)
        record = response['data']['items'][0]
        return record
    
    def push_field(self, field) -> dict or None :
        field.options = json.dumps(field.options)
        field.content = json.dumps(field.content)
        data = {
            "record" : field.record_id,
            "type" : field.field_type,
            "content" : field.content,
            "options" : field.options
        }
        response = self.post(self.create_field_url, data)
        field = response['data']['items'][0]
        return field
