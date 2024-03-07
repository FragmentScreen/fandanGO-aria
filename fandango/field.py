from .utils import *
from .config import *

class Fields :

    def __init__(self, token) : 
        self.token = token
        self.record_id = []
        self.fields = []
        self.headers = set_headers(token)
        self.options = ['TestFieldType', 'OtherFieldType']
        self.list_url_base = f'http://localhost:8281/api/v1/field?filter[record]='
        self.list_url = f'http://localhost:8281/api/v1/field?filter[record]='
        self.create_url = 'http://localhost:8281/api/v1/createDataField'


    def populate_fields_for_records(self) :
        for record in self.record_id :
            self.list_url = f"{self.list_url_base}{record['id']}"
            print(self.list_url)
            fields = self.list_fields()
            for field in fields :
                self.fields.append(field)




    def create_field(self, record_id, data):
        fields = self.get_input_fields(record_id, data)
        resp = requests.post(self.create_url, fields, headers=self.headers)
        resp.raise_for_status()
        resp = resp.json()
        field = resp['data']['items']
        self.fields.append(field)
    
    def list_fields(self):
        # self.generate_url()
        resp = requests.get(self.list_url, headers=self.headers)
        resp.raise_for_status()
        resp = resp.json()

        return resp['data']['items']

    
    def get_input_fields(self, record_id, fields=None):
        fields['record'] = record_id
        fields['content'] = json.dumps(fields['content'])
        return fields
    
    # def get_fields_data(self) :
    #     type = command_with_options('Select Field Type', self.options)
    #     options = self.options_manager()
    #     content = click.prompt('Enter content')
    #     content = json.dumps(content)
    #     return {
    #         "record" : self.record_id,
    #         "content" : content,
    #         "type" : type,
    #         "options" : options
    #     }

    
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


        