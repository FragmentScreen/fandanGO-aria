from .field import Field
from .bucket import Bucket
from .record import Record
from .api_client import APIClient
from .imports_config import *
from .utils import get_config
from dotenv import load_dotenv

load_dotenv()
class DataManagerClient(APIClient):
    def __init__(self, token, entity_id, entity_type):
        super().__init__(token)
        self.token = token
        self.pull_buckets_url = os.getenv('ARIA_ENDPOINTS_PULL_BUCKETS')
        self.pull_records_url = os.getenv('ARIA_ENDPOINTS_PULL_RECORDS')
        self.pull_fields_url = os.getenv('ARIA_ENDPOINTS_PULL_FIELDS')
        self.create_bucket_url = os.getenv('ARIA_ENDPOINTS_CREATE_BUCKET')
        self.create_record_url = os.getenv('ARIA_ENDPOINTS_CREATE_RECORD')
        self.create_field_url = os.getenv('ARIA_ENDPOINTS_CREATE_FIELD')
        self.base_url = os.getenv('ARIA_DATA_DEPOSITION_URL')
        self.id = entity_id
        self.type = entity_type

    # BUCKETS
        
    def push_bucket(self, bucket : Bucket) -> Union[dict, None] :
        data = {
            'aria_id': bucket.entity_id,
            "aria_entity_type" : bucket.entity_type, 
            'embargoed_until' : bucket.embargo_date
        }
        response = self.post(self.create_bucket_url, data)
        bucket = response['data']['items'][0]
        return bucket
    
    def pull_buckets(self, id : int, type : str) : 
        data = {
            'aria_id' : id,
            'aria_entity_type': type
        }
        response = self.get(self.pull_buckets_url, data)
        buckets = response['data']['items']
        return buckets
    
    # RECORDS
    
    def push_record(self, record : Record) -> Union[dict, list] :
        data = {
            "bucket" : record.bucket_id,
            "schema" : record.schema_type
        }
        response = self.post(self.create_record_url, data)
        record = response['data']['items'][0]
        return record

    def pull_records(self, bucket_id : str) : 
        data = {
            'bucket' : bucket_id,
        }
        response = self.get(self.pull_records_url, data)
        records = response['data']['items']
        return records

    # FIELDS 

    def push_field(self, field : Field) -> Union[dict, None] :
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
    
    def pull_fields(self, record_id : str) : 
        data = {
            'record' : record_id,
        }
        response = self.get(self.pull_fields_url, data)
        records = response['data']['items']
        return records


    

