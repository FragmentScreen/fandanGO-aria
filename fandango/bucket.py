from .config import *
from .utils import *
from .abstract_bucket import AbstractBucket

class Bucket(AbstractBucket):
    
    def __init__(self, entity_id : int, entity_type : str, embargo_date : str, **kwargs):
        self._entity_type = entity_type
        self._entity_id = entity_id
        self._embargo_date = embargo_date
        self._id = kwargs.get('id')
        self._owner = kwargs.get('owner')
        self._created = kwargs.get('created')
        self._updated = kwargs.get('updated')

    @property
    def entity_type(self):
        """Getter for the entity type."""
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        """Setter for the entity type."""
        self._entity_type = value

    @property
    def entity_id(self):
        """Getter for the entity ID."""
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        """Setter for the entity ID."""
        self._entity_id = value

    @property
    def embargo_date(self):
        """Getter for the embargo date."""
        return self._embargo_date

    @embargo_date.setter
    def embargo_date(self, value):
        """Setter for the embargo date."""
        self._embargo_date = value

    @property
    def id(self):
        """Getter for the Bucket ID."""
        return self._id
    
    @id.setter
    def id(self, value):
        """Setter for the Bucket ID."""
        self._id = value    
    
    @property
    def owner(self):
        """Getter for the owner."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """Setter for the owner."""
        self._owner = value

    @property
    def created(self):
        """Getter for the Created Date"""
        return self._created

    @created.setter
    def created(self, value):
        """Setter for the created date."""
        self._created = value

    @property
    def updated(self):
        """Getter for the updated date."""
        return self._updated

    @updated.setter
    def updated(self, value):
        """Setter for the updated date."""
        self._updated = value

    # def __setattr__(self, name, value):
    #     properties = ['entity_type', '_entity_id', '_embargo_date', '_bucket_id', '_owner', '_created', '_updated']
    #     if name not in properties:
    #         raise AttributeError(f"Cannot set attribute '{name}'. It's not defined in __init__.")
    #     super().__setattr__(name, value)

    def populate(self,data):
        """Generate additional properties like bucket ID, owner, created, and updated."""
        self.id = data['id']
        self.owner = data['owner']
        self.created = data['created']
        self.updated = data['updated']


    # def __init__(self,token, bucket_id) -> None :
    #     self.token = token
    #     self.headers = set_headers(self.token)
    #     self.id = bucket_id
    #     self.bucket = None


    
    # # def populate(self) :
    # #     url = f'http://localhost:8281/api/v1/bucket?filter[id]={self.id}'
    # #     response = requests.get(url, headers=self.headers)
    # #     response.raise_for_status()
    # #     response = response.json()
    # #     bucket = response['data']['items'][0]
    # #     self.bucket = bucket
    # #     print(f'populate success for Bucket ID: {self.id}')

    
    # # def list_buckets(self) -> str | None : 
    # #     some_url = 'http://localhost:8281/api/v1/bucket'
    # #     response = requests.get(some_url, headers=self.headers)
    # #     response.raise_for_status()
    # #     return response.json()
    
    # # def select_bucket(self) :
    # #     buckets = self.list_buckets()
    # #     bucket_options = buckets['data']['items']
    # #     bucket_fields = ['id','aria_entity_type', 'embargoed_until', 'created']
    # #     bucket = command_with_options('select the bucket', bucket_options, True, bucket_fields)
    # #     self.id = bucket['id']
    # #     return bucket
        

    # # def get_fields(self) -> json :
    # #     aria_id = click.prompt('Set ARIA ID', type=int)
    # #     options = ['proposal', 'field']
    # #     aria_entity = command_with_options('aria entity', options)
    # #     embargoed_until = click.prompt('Emargoed Until (dd/mm/yy)', type=click.DateTime(formats=['%d/%m/%y']), default='', show_default=False)
    # #     embargoed_until = format_datetime_to_json_serializable(embargoed_until)
    # #     return {
    # #         'aria_id': aria_id,
    # #         "aria_entity_type" : aria_entity, 
    # #         'embargoed_until' : embargoed_until
    # #     }




