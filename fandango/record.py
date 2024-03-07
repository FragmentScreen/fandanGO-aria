from .config import *
from .utils import *

class Records :
    def __init__(self, token) : 
        self.token = token
        self.bucket_id = None
        self.records = None

    def get_records(self) : 
        some_url = f'http://localhost:8281/api/v1/record?filter[bucket]={self.bucket_id}' 
        headers = set_headers(self.token)
        resp = requests.get(some_url, headers=headers)
        resp.raise_for_status()
        resp = resp.json()
        records = resp['data']['items']
        self.records = records
        return records
    
    def print_class_info(self):
        pretty_print({'bucket': self.bucket_id, 'records': self.records})

    def create_record(self, input_fields) :
        some_url = 'http://localhost:8281/api/v1/createDataRecord'
        headers = set_headers(self.token)
        fields = self.get_fields(fields) if not input_fields else input_fields
        fields['bucket'] = self.bucket_id
        resp = requests.post(some_url, fields, headers=headers)
        # resp.raise_for_status()
        resp = resp.json()
        records = resp['data']['items']
        self.records = records

    def populate_records(self) :
        some_url = f'http://localhost:8281/api/v1/record?filter[bucket]={self.bucket_id}' 
        headers = set_headers(self.token)
        resp = requests.get(some_url, headers=headers)
        resp.raise_for_status()
        resp = resp.json()
        self.records = resp['data']['items']


    def select_record(self) :
        records = self.get_records()
        record_fields = ['id', 'schema', 'created']
        record = command_with_options('select the record',records['data']['items'], True, record_fields)
        return record

    def get_fields(self) -> str :
        options = ['TestSchema', 'OtherSchema']
        schema = command_with_options('Schema Type', options)
        return {
            'schema': schema, 
        }
