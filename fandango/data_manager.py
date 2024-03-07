from .config import * 
from .utils import pretty_print, print_with_spaces
from .bucket import Bucket
from .record import Records
from .field import Fields

class DataManager:
    def __init__(self, token, bucket_id):
        self.bucket_manager = Bucket(token, bucket_id)
        self.records_manager = Records(token)
        self.fields = []
        if bucket_id is not None :
            self.populate(bucket_id)

    def create_bucket(self, fields) :
        self.bucket_manager.create_bucket(fields)
        self.records_manager.bucket_id = self.bucket_manager.bucket['id']


    def populate(self, bucket_id) :
        self.bucket_manager.populate()
        self.records_manager.bucket_id = bucket_id
        self.records_manager.records = self.list_records_for_bucket()


    # def check_bucket_exists(self) :
    #     return True if self.bucket_manager.bucket else False

    def list_records_for_bucket(self) :
        # if not self.check_bucket_exists() :
        #     return False
        return self.records_manager.get_records()
    
    def print_records(self) :
        pretty_print(self.records_manager.records)

    
    def print_bucket_info(self) :
        if self.bucket_manager :
            bucket = self.bucket_manager.bucket
            print_with_spaces(f'Bucket info for ID: {self.bucket_manager.id}')
            pretty_print(bucket)
        else :
            print('No bucket set')
    
    def list_buckets(self):
        buckets = self.bucket.list_buckets()
        pretty_print(buckets)


    def create_record(self, fields):
        self.records_manager.create_record(fields)
    # def create_record(self):
    #     self.records.create_record()
    
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

    # def select_bucket(self) : 
    #     bucket = self.bucket.select_bucket()
    #     self.records.bucket_id = bucket['id']

    # def list_records(self):
    #     self.select_bucket()
    #     self.records.get_records()

    # def list_all_entity_fields
        
    # def create_bucket(self)
        # self.bucket = new_bucket.create_bucket(fields)
        # self.bucket.create_bucket(fields)

# may want to turn these into subclasses where bucket consumes record, consumes field 