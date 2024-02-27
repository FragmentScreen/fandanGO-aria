from ..config import * 
from ..utils import pretty_print, set_headers
from .bucket import Bucket

class DataManager:
    def __init__(self):
        self.bucket = Bucket()

    # def create_bucket(self, fields, token) -> None :
    #     # need to add click input 
    #     fields = {'aria_id': 12, "aria_entity_type" : 'visit', 'embargoed_until' : '2040-02-19 12:00:00'}
    #     headers = set_headers(token)
    #     some_url = 'http://localhost:8281/api/v1/createDataBucket'
    #     response = requests.post(some_url, json=fields, headers=headers)
    #     response.raise_for_status()
    #     resp = response.json()
    #     pretty_print(resp)
    #     pass
        
    def create_bucket(self, token) : 
        self.bucket.create_bucket(token)

    
    
    def list_buckets(self, token):
        headers = set_headers(token)
        some_url = 'http://localhost:8281/api/v1/bucket'
        response = requests.get(some_url, headers=headers)
        response.raise_for_status()
        resp = response.json()
        pretty_print(resp)
        pass
    
    def create_record(self, token, bucket_id='3274f598-6eb5-4209-bf9b-a0305f4835ee', record_data=None,):
        some_url = 'http://localhost:8281/api/v1/createDataRecord'
        print(token)
        headers = set_headers(token)
        schema = 'TestSchema'
        context = None
        resp = requests.post(some_url, {'schema' : schema, 'bucket': bucket_id}, headers=headers)
        resp.raise_for_status()
        resp = resp.json()
        pretty_print(resp)
        pass
    
    def list_records(self, token):
        some_url = 'http://localhost:8281/api/v1/record'
        headers = set_headers(token)
        resp = requests.get(some_url, headers=headers)
        resp.raise_for_status()
        resp = resp.json()
        pretty_print(resp)
        pass
    
    def create_field(self, token):
        some_url = 'http://localhost:8281/api/v1/createDataField'
        headers = set_headers(token)
        record = "d7f7be48-24c4-4440-83ca-dc46cff2c596"
        type = "TestFieldType"
        content = "hello lui"
        content = json.dumps(content)
        options = {"option" : "Lui"}
        options = json.dumps(options)
        stuff = {"record": "d7f7be48-24c4-4440-83ca-dc46cff2c596","content": content, "type": "TestFieldType", "options": options}
        # stuff = json.dumps(stuff)
        resp = requests.post(some_url, stuff, headers=headers)
        # resp.raise_for_status()
        resp = resp.json()
        pretty_print(resp)
        pass
    
    def list_fields(self, token):
        some_url = 'http://localhost:8281/api/v1/field?record=d7f7be48-24c4-4440-83ca-dc46cff2c596'
        headers = set_headers(token)
        resp = requests.get(some_url, headers=headers)
        resp.raise_for_status()
        resp = resp.json()
        pretty_print(resp)
        pass

# may want to turn these into subclasses where bucket consumes record, consumes field 