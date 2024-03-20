from .utils import *
from .config import *
from .abstract_field import AbstractField

class Field(AbstractField) :
    def __init__(self, record_id: str, field_type : str, content : str, options : dict = None, order: int = 0, **kwargs):
        self._record_id = record_id
        self._field_type = field_type
        self._content = content
        self._options = options if options is not None else {}
        self._order = order
        self._id = kwargs.get('id')
        

    @property
    def record_id(self):
        """Getter for the Field's Record ID."""
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        """Setter for the Field's Record ID."""
        self._record_id = value

    @property
    def field_type(self):
        """Getter for the Field Type."""
        return self._field_type

    @field_type.setter
    def field_type(self, value):
        """Setter for the Field Type."""
        self._field_type = value

    @property
    def content(self):
        """Getter for the Field Content."""
        return self._content

    @content.setter
    def content(self, value):
        """Setter for the Field Content."""
        self._content = value

    @property
    def options(self):
        """Getter for the Field Options."""
        return self._options

    @options.setter
    def options(self, value):
        """Setter for the Field Options."""
        self._options = value

    @property
    def order(self):
        """Getter for the Field Order."""
        return self._order

    @order.setter
    def order(self, value):
        """Setter for the Field Order."""
        self._order = value
    
    @property
    def id(self):
        """Getter for the Field ID."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for the Field ID."""
        self._id = value

    def populate(self, data):
        """Populate field with additional properties after pushing to the database."""
        self._id = data.get('id')

    # def __init__(self, token) : 
    #     self.token = token
    #     self.record_id = []
    #     self.fields = []
    #     self.headers = set_headers(token)
    #     self.options = ['TestFieldType', 'OtherFieldType']
    #     self.list_url_base = f'http://localhost:8281/api/v1/field?filter[record]='
    #     self.list_url = f'http://localhost:8281/api/v1/field?filter[record]='
    #     self.create_url = 'http://localhost:8281/api/v1/createDataField'


    # def populate_fields_for_records(self) :
    #     for record in self.record_id :
    #         self.list_url = f"{self.list_url_base}{record['id']}"
    #         fields = self.list_fields()
    #         for field in fields :
    #             self.fields.append(field)

    # def create_field(self, record_id, data):
    #     fields = self.get_input_fields(record_id, data)
    #     resp = requests.post(self.create_url, fields, headers=self.headers)
    #     resp.raise_for_status()
    #     resp = resp.json()
    #     field = resp['data']['items'][0]
    #     self.fields.append(field)
    
    # def list_fields(self):
    #     resp = requests.get(self.list_url, headers=self.headers)
    #     resp.raise_for_status()
    #     resp = resp.json()
    #     return resp['data']['items']

    
    # def get_input_fields(self, record_id, fields=None):
    #     if fields is None :
    #         fields = self.get_fields_data()
    #     fields['record'] = record_id
    #     fields['content'] = json.dumps(fields['content'])
    #     fields['options'] = json.dumps(fields['options'])
    #     return fields
    
    # def get_fields_data(self) :
    #     type = command_with_options('Select Field Type', self.options)
    #     options = self.options_manager()
    #     content = click.prompt('Enter content')
    #     return {
    #         "content" : content,
    #         "type" : type,
    #         "options" : options
    #     }
    
    # def print_fields(self, record_id) : 
    #     if not record_id :
    #         pretty_print(self.fields)
    #         return
    #     selection = []
    #     for field in self.fields :
    #         if field['record'] == record_id:
    #             selection.append(field)
    #     pretty_print(selection)

    
    # def options_manager(self, options={}):
    #     if click.confirm('Would you like to add an option key-value?'):
    #         key = click.prompt('Enter Key Name')
    #         value = click.prompt(f'Enter Value for {key}')
    #         options[key] = value
    #         return self.options_manager(options)
    #     else:
    #         return options
        


        