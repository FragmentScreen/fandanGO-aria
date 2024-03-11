from .config import *
from .utils import *
from .abstract_bucket import AbstractBucket

class Bucket(AbstractBucket):
    def __init__(self, entity_id : int, entity_type : str, embargo_date : str):
        self._entity_type = entity_type
        self._entity_id = entity_id
        self._embargo_date = embargo_date
        self._bucket_id = None
        self._owner = None
        self._created = None
        self._updated = None

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

    def populate(self,data):
        """Generate additional properties like bucket ID, owner, created, and updated."""
        self._bucket_id = data['id']
        self._owner = data['owner']
        self._created = data['created']
        self._updated = data['updated']


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




