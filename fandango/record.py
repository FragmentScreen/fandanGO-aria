from .config import *
from .abstract_record import AbstractRecord
from .utils import *

class Record(AbstractRecord):
    def __init__(self, bucket_id: str, schema: str):
        self._bucket_id = bucket_id
        self._schema_type = schema
        self._id = None
        self._owner = None
        self._created = None
        self._updated = None

    @property
    def bucket_id(self):
        """Getter for the Bucket ID."""
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, value):
        """Setter for the Bucket ID."""
        self._bucket_id = value

    @property
    def schema_type(self):
        """Getter for the Schema Type."""
        return self._schema_type

    @schema_type.setter
    def schema_type(self, value):
        """Setter for the Schema Type."""
        self._schema_type = value

    @property
    def id(self):
        """Getter for the Record ID."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for the Record ID."""
        self._id = value

    @property
    def owner(self):
        """Getter for the Record owner."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """Setter for the Record owner."""
        self._owner = value

    @property
    def created(self):
        """Getter for the Record created timestamp."""
        return self._created

    @created.setter
    def created(self, value):
        """Setter for the Record created timestamp."""
        self._created = value

    @property
    def updated(self):
        """Getter for the Record updated timestamp."""
        return self._updated

    @updated.setter
    def updated(self, value):
        """Setter for the Record updated timestamp."""
        self._updated = value

    def populate(self, data):
        """Populate record with additional properties."""
        self._id = data.get('id')
        self._owner = data.get('owner')
        self._created = data.get('created')
        self._updated = data.get('updated')
        
   
   
    # def __init__(self, token) : 
    #     self.token = token
    #     self.bucket_id = None
    #     self.records = []

    # def get_records(self) : 
    #     some_url = f'http://localhost:8281/api/v1/record?filter[bucket]={self.bucket_id}' 
    #     headers = set_headers(self.token)
    #     resp = requests.get(some_url, headers=headers)
    #     resp.raise_for_status()
    #     resp = resp.json()
    #     records = resp['data']['items']
    #     self.records = records
    #     return records
    
    # def print_class_info(self):
    #     pretty_print({'bucket': self.bucket_id, 'records': self.records})

    # def create_record(self, input_fields) :
    #     some_url = 'http://localhost:8281/api/v1/createDataRecord'
    #     headers = set_headers(self.token)
    #     fields = self.get_fields() if not input_fields else input_fields
    #     fields['bucket'] = self.bucket_id
    #     resp = requests.post(some_url, fields, headers=headers)
    #     resp.raise_for_status()
    #     resp = resp.json()
    #     record = resp['data']['items'][0]
    #     self.records.append(record)
    #     return record['id']

    # def populate_records(self) :
    #     some_url = f'http://localhost:8281/api/v1/record?filter[bucket]={self.bucket_id}' 
    #     headers = set_headers(self.token)
    #     resp = requests.get(some_url, headers=headers)
    #     resp.raise_for_status()
    #     resp = resp.json()
    #     self.records = resp['data']['items']


    # def select_record(self) :
    #     record_fields = ['id', 'schema', 'created']
    #     record = command_with_options('select the record',self.records, True, record_fields)
    #     return record

    # def get_fields(self) -> str :
    #     options = ['TestSchema', 'OtherSchema']
    #     schema = command_with_options('Schema Type', options)
    #     return {
    #         'schema': schema, 
    #     }
