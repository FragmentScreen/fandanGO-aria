from ..utils import *
from ..config import *

class Fields :

    def __init__(self, token) : 
        self.token = token
        self.record_id = None
        self.headers = set_headers(token)
        self.options = ['TestFieldType', 'OtherFieldType']
        self.list_url = f'http://localhost:8281/api/v1/field?filter[record]={self.record_id}'
        self.create_url = 'http://localhost:8281/api/v1/createDataField'



    def create_field(self):
        fields = self.get_fields_data()
        resp = requests.post(self.create_url, fields, headers=self.headers)
        # resp.raise_for_status()
        resp = resp.json()
        print_with_spaces(f'New Field for Record {self.record_id} created:')
        pretty_print(resp['data']['items'])
    
    def list_fields(self):
        self.generate_url()
        resp = requests.get(self.list_url, headers=self.headers)
        resp.raise_for_status()
        resp = resp.json()
        pretty_print(resp)
        pass

    def get_fields_data(self) :
        type = command_with_options('Select Field Type', self.options)
        options = self.options_manager()
        content = click.prompt('Enter content')
        content = json.dumps(content)
        return {
            "record" : self.record_id,
            "content" : content,
            "type" : type,
            "options" : options
        }

    
    def options_manager(self, options={}):
        if click.confirm('Would you like to add an option key-value?'):
            key = click.prompt('Enter Key Name')
            value = click.prompt(f'Enter Value for {key}')
            options[key] = value
            return self.options_manager(options)
        else:
            return json.dumps(options)
        
    def generate_url(self) :
        self.list_url = f'http://localhost:8281/api/v1/field?filter[record]={self.record_id}'


        