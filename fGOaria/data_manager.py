from .imports_config import * 
from .utils import pretty_print, print_with_spaces, print_created_message
from .bucket import Bucket
from .record import Record 
from .field import Field
from .client_data_manager import DataManagerClient as DataClient
class DataManager:
    def __init__(self, token, entity_id : int, entity_type : str, populate : bool) :
        """Initiate a new DataManager for Entity ID & Type's Buckets, Records & Fields"""

        self.entity_type = entity_type
        self.entity_id = entity_id
        self.buckets = {}
        self.records = {}
        self.fields = {}
        self.client = DataClient(token, entity_id, entity_type)

        if populate :
            self.populate()

    def create_bucket(self, embargo : str) -> Bucket : 
        """Create a bucket and push to the DataManager Class Buckets dictionary"""

        bucket = Bucket(self.entity_id, self.entity_type, embargo)
        created_bucket = self.client.push_bucket(bucket)
        bucket.populate(created_bucket)
        self.buckets[bucket._id] = bucket
        return bucket

    def push(self, obj) -> None:
        """Push an object to the appropriate client endpoint"""

        if isinstance(obj, Bucket):
            new_bucket = self.client.push_bucket(obj)
            obj.populate(new_bucket)
            self.buckets[obj._id] = obj
        elif isinstance(obj, Record):
            new_record = self.client.push_record(obj)
            obj.populate(new_record)
            self.records[obj._id] = obj
        elif isinstance(obj, Field):
            new_field = self.client.push_field(obj)
            obj.populate(new_field)
            self.fields[obj._id] = obj
        else:
            raise ValueError("Unsupported object type for pushing")

    def create_record(self, bucket_id : str, schema_type : str) -> Record : 
        """Create a record and push to the DataManager Class Records dictionary"""

        record = Record(bucket_id, schema_type)
        created_record = self.client.push_record(record)
        record.populate(created_record)
        self.records[record.id] = record
        return record
    
    def create_field(self, record_id: str, type: str, content: str, options: dict = None) -> Field :
        """Create a field and push to the DataManager Class Fields dictionary"""

        field = Field(record_id, type, content, options)
        created_field = self.client.push_field(field)
        field.populate(created_field)
        self.fields[field.id] = field
        return field

    def populate(self) -> None : 
        """Populate new Bucket classes and add to Data Manager based on API request"""

        buckets = self.client.pull_buckets(self.entity_id, self.entity_type)
        for b in buckets : 
            new_bucket = Bucket(b['aria_id'], b['aria_entity_type'], b['embargoed_until'], id=b['id'], owner=b['owner'], created=b['created'], updated=b['updated'])
            self.buckets[b['id']] = new_bucket
        
        for bucket_id, obj in self.buckets.items():
            records = self.client.pull_records(bucket_id)
            if records != [] :
                for r in records :
                    new_record = Record(r['bucket'], r['schema'])
                    new_record.populate(r)
                    self.records[r['id']] = new_record

        for record_id, obj in self.records.items():
            fields = self.client.pull_fields(record_id)
            if fields != [] :
                for field in fields :
                    new_field = Field(field['record'], field['type'], field['content'], field['options'], field['order'], id=field['id'])
                    self.fields[field['id']] = new_field

