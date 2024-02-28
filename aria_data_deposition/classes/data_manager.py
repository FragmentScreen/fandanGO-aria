from ..config import * 
from ..utils import pretty_print, set_headers
from .bucket import Bucket
from .record import Records
from .field import Fields

class DataManager:
    def __init__(self, token):
        self.token = token
        self.bucket = Bucket(self.token)
        self.records = Records(self.token)
        self.fields = Fields(self.token)

    def create_bucket(self) : 
        self.bucket.create_bucket()
    
    def list_buckets(self):
        buckets = self.bucket.list_buckets()
        pretty_print(buckets)

    def list_records(self):
        self.select_bucket()
        self.records.get_records()
    
    def create_record(self):
        self.select_bucket()
        self.records.create_record()

    def select_bucket(self) : 
        bucket = self.bucket.select_bucket()
        self.records.bucket_id = bucket['id']
    
    def select_record(self) :
        self.select_bucket()
        record = self.records.select_record()
        self.fields.record_id = record['id']

    def create_field(self):
        self.select_record()
        self.fields.create_field()
    
    def list_fields(self):
        self.select_record()
        self.fields.list_fields()

# may want to turn these into subclasses where bucket consumes record, consumes field 