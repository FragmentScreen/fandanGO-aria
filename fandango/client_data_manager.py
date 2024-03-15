import requests
from .api_client import APIClient
from .config import *
from .utils import set_headers, pretty_print, get_config

config = get_config()
class DataManagerClient(APIClient):
    def __init__(self, token, entity_id, entity_type):
        super().__init__(token)
        self.token = token
        self.pull_buckets_url = config["endpoints"]["get"]["bucket"]
        self.pull_records_url = config["endpoints"]["get"]["record"]
        self.pull_fields_url = config["endpoints"]["get"]["field"]
        self.create_bucket_url = config["endpoints"]["create"]['bucket']
        self.create_record_url = config["endpoints"]['create']['record']
        self.create_field_url = config["endpoints"]['create']['field']

        self.id = entity_id
        self.type = entity_type

    # BUCKETS
        
    def push_bucket(self, bucket) -> dict | None :
        data = {
            'aria_id': bucket.entity_id,
            "aria_entity_type" : bucket.entity_type, 
            'embargoed_until' : bucket.embargo_date
        }
        response = self.post(self.create_bucket_url, data)
        bucket = response['data']['items'][0]
        return bucket
    
    def pull_buckets(self, id : int, type : str) -> list[dict[str, any]] or [] : 
        data = {
            'aria_id' : id,
            'aria_entity_type': type
        }
        response = self.get(self.pull_buckets_url, data)
        buckets = response['data']['items']
        return buckets
    
    # RECORDS
    
    def push_record(self, record) -> dict or None :
        data = {
            "bucket" : record.bucket_id,
            "schema" : record.schema_type
        }
        response = self.post(self.create_record_url, data)
        record = response['data']['items'][0]
        return record

    def pull_records(self, bucket_id : str) -> list[dict[str, any]] or [] : 
        data = {
            'bucket' : bucket_id,
        }
        response = self.get(self.pull_records_url, data)
        records = response['data']['items']
        return records

    # FIELDS 

    def push_field(self, field) -> dict or None :
        # field.options = json.dumps(field.options)
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
    
    def pull_fields(self, record_id : str) -> list[dict[str, any]] or [] : 
        data = {
            'record' : record_id,
        }
        response = self.get(self.pull_fields_url, data)
        records = response['data']['items']
        return records


    

