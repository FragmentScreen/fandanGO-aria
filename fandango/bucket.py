from .config import *
from .utils import *

class Bucket :

    def __init__(self,token, bucket_id) -> None :
        self.token = token
        self.headers = set_headers(self.token)
        self.id = bucket_id
        self.bucket = None

    def create_bucket(self, fields=None) -> dict | None :
        if not fields :
            fields = self.get_fields()
        some_url = 'http://localhost:8281/api/v1/createDataBucket'
        response = requests.post(some_url, json=fields, headers=self.headers)
        response.raise_for_status()
        response = response.json()
        bucket = response['data']['items'][0]
        self.bucket = bucket
        return bucket
    
    def populate(self) :
        url = f'http://localhost:8281/api/v1/bucket?filter[id]={self.id}'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        response = response.json()
        bucket = response['data']['items'][0]
        self.bucket = bucket
        print(f'populate success for Bucket ID: {self.id}')

    
    def list_buckets(self) -> str | None : 
        some_url = 'http://localhost:8281/api/v1/bucket'
        response = requests.get(some_url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def select_bucket(self) :
        buckets = self.list_buckets()
        bucket_options = buckets['data']['items']
        bucket_fields = ['id','aria_entity_type', 'embargoed_until', 'created']
        bucket = command_with_options('select the bucket', bucket_options, True, bucket_fields)
        return bucket
        

    def get_fields(self) -> json :
        aria_id = click.prompt('Set ARIA ID', type=int)
        options = ['proposal', 'field']
        aria_entity = command_with_options('aria entity', options)
        embargoed_until = click.prompt('Emargoed Until (dd/mm/yy)', type=click.DateTime(formats=['%d/%m/%y']), default='', show_default=False)
        embargoed_until = format_datetime_to_json_serializable(embargoed_until)
        return {
            'aria_id': aria_id,
            "aria_entity_type" : aria_entity, 
            'embargoed_until' : embargoed_until
        }



