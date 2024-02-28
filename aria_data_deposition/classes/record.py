from ..config import *
from ..utils import *

class Records :
    def __init__(self, token) : 
        self.token = token
        self.bucket_id = None

    def get_records(self) : 
        some_url = f'http://localhost:8281/api/v1/record?filter[bucket]={self.bucket_id}' 
        print(some_url)
        headers = set_headers(self.token)
        resp = requests.get(some_url, headers=headers)
        resp.raise_for_status()
        resp = resp.json()
        return resp

    def create_record(self) :
        some_url = 'http://localhost:8281/api/v1/createDataRecord'
        headers = set_headers(self.token)
        fields = self.get_fields()
        resp = requests.post(some_url, fields, headers=headers)
        resp.raise_for_status()
        resp = resp.json()
        pretty_print(resp)

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
            "bucket" : self.bucket_id, 
        }
