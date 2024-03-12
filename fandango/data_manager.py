from .config import * 
from .utils import pretty_print, print_with_spaces
from .bucket import Bucket
from .record import Record 
from .field import Field
from .client_data_manager import DataManagerClient as EntityClient
class DataManager:
    def __init__(self, token, entity_id, entity_type, populate=False) :
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.buckets = {}
        self.records = {}
        self.fields = {}
        self.client = EntityClient(token, entity_id, entity_type)

    def create_bucket(self, embargo : str) -> None : 
        """Create a bucket and push to the DataManager Class Buckets dictionary"""

        bucket = Bucket(self.entity_id, self.entity_type, embargo)
        created_bucket = self.client.push_bucket(bucket)
        bucket.populate(created_bucket)
        self.buckets[bucket._bucket_id] = bucket


    def create_record(self, bucket_id : str, schema_type : str) -> None : 
        """Create a record and push to the DataManager Class Records dictionary"""

        record = Record(bucket_id, schema_type)
        created_record = self.client.push_record(record)
        record.populate(created_record)
        self.records[record.id] = record
        return record
    
    def create_field(self, record_id: str, type: str, content: str, options: dict = None) -> None :
        """Create a field and push to the DataManager Class Fields dictionary"""

        field = Field(record_id, type, content, options)
        created_field = self.client.push_field(field)
        field.populate(created_field)
        self.fields[field.id] = field


    
    

    # def __init__(self, token, bucket_id):
    #     self.bucket_manager = Bucket(token, bucket_id)
    #     self.records_manager = Records(token)
    #     self.fields_manager = Fields(token)
    #     if bucket_id is not None :
    #         self.populate(bucket_id)

    # # check commit working
    # # BUCKET

    # def create_bucket(self, fields=None) :
    #     bucket = self.bucket_manager.create_bucket(fields)
    #     self.records_manager.bucket_id = bucket['id']
    #     return bucket['id']
    
    # def select_bucket(self) : 
    #     bucket = self.bucket_manager.select_bucket()
    #     bucket_id = bucket['id']
    #     self.populate(bucket_id)
    #     return bucket_id
    
    # def print_bucket_info(self) :
    #     if self.bucket_manager.bucket :
    #         bucket = self.bucket_manager.bucket
    #         records = self.records_manager.records
    #         fields = self.fields_manager.fields
    #         print_with_spaces(f"Bucket info for ID: {self.bucket_manager.bucket['id']}")
    #         pretty_print({'Bucket' : bucket, 'Records' : records, 'Fields': fields })
    #     else :
    #         print('No bucket set')


    # # RECORDS 

    # def get_records_for_bucket(self) :
    #     return self.records_manager.get_records()
    
    # def print_records(self) :
    #     pretty_print(self.records_manager.records)

    # def create_record(self, fields=None):
    #     record_id = self.records_manager.create_record(fields)
    #     return record_id
    
    # def select_record(self) :
    #     record = self.records_manager.select_record()
    #     self.fields_manager.record_id = record['id']
    #     return self.fields_manager.record_id
    
    # def get_fields_for_records(self) :
    #     pretty_print(self.fields_manager.fields)
    


    




    
    # def select_record(self) :
    #     # self.select_bucket()
    #     record = self.records_manager.select_record()
    #     self.fields_manager.record_id = record['id']
    #     return self.fields_manager.record_id

    # def create_field(self, record_id=None, data=None):
    #     # self.select_record()
    #     self.fields_manager.create_field(record_id, data)
    
    # def list_fields(self):
    #     self.select_record()
    #     self.fields.list_fields()


    # # INITIATOR (When bucket_id supplier)

    # def populate(self, bucket_id) :
    #     self.bucket_manager.populate()
    #     self.records_manager.bucket_id = bucket_id
    #     self.records_manager.records= self.get_records_for_bucket()
    #     self.fields_manager.record_id  = self.records_manager.records
    #     self.fields_manager.populate_fields_for_records()