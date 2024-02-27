from ..config import *
from ..utils import *

class Bucket :

    def __init__(self) -> None :
        self.id = None
        self.records = []

    def create_bucket(self, token) -> dict | None :
        headers = set_headers(token)
        fields = self.get_fields()
        some_url = 'http://localhost:8281/api/v1/createDataBucket'
        response = requests.post(some_url, json=fields, headers=headers)
        resp = response.json()
        return resp

    def get_fields(self) -> json :
        aria_id = click.prompt('Set ARIA ID', type=int)
        options = ['proposal', 'field']
        aria_entity = command_with_options('aria entity', options)
        embargoed_until = click.prompt('Emargoed Until (dd/mm/yy)', type=click.DateTime(formats=['%d/%m/%y']), default='', show_default=False)
        embargoed_until = format_datetime_to_json_serializable(embargoed_until)
        print(embargoed_until)
        return {
            'aria_id': aria_id,
            "aria_entity_type" : aria_entity, 
            'embargoed_until' : embargoed_until
        }



