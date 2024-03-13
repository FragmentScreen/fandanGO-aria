from .data_manager import DataManager
from .utils import *
import click

class DataManagerCLI(DataManager):
    def __init__(self, token, entity_id, entity_type, populate):
        super().__init__(token, entity_id, entity_type, populate)

    def menu(self) : 
        action = command_with_options('What would you like to do?', ['Create', 'Print', 'Exit'])
        if action == 'Exit': 
            print('Ciao!')
            return
        data = command_with_options(f'What would you like to {action.lower()}?', ['Bucket', 'Record', 'Field'])
        if action == 'Create' :
            self.creator_cli(data)
        elif action == 'Print' :
            self.printer_cli(data)

    # CREATE 
            
    def creator_cli(self, data) :
        if data == 'Bucket' :
            self.create_bucket_cli()
        if data == 'Record' :
            self.create_record_cli()
        if data == 'Field' :
            self.create_field_cli()

    def create_bucket_cli(self, menu_return=True) :
        embargo= click.prompt('Emargoed Until (dd/mm/yy)', type=click.DateTime(formats=['%d/%m/%y']), default='', show_default=False)
        embargo = format_datetime_to_json_serializable(embargo)
        bucket = self.create_bucket(embargo)
        print(f"Bucket created with ID: {bucket.bucket_id}")
        if menu_return :
            return self.menu()
        else:
            return bucket.bucket_id 
        
    def create_record_cli(self, menu_return=True):
        existing_bucket = click.confirm('Create record for existing Bucket?')
        if not existing_bucket :
            bucket_id = self.create_bucket_cli(False)
        else : 
            bucket_id = self.select_bucket_cli()
        schema = command_with_options('Select Schema Type', ['TestSchema', 'WrongSchema'])
        record = self.create_record(bucket_id, schema)
        if menu_return : 
            self.menu()
        else :
            return record.id
    
    def create_field_cli(self, menu_return=True) :
        existing_record = click.confirm('Create field for existing Record?')
        if not existing_record :
            record_id = self.create_record(False)
        else :
            bucket_id = self.select_bucket_cli()
            record_id = self.select_record_cli(bucket_id)
        type = command_with_options('Select Field Type', ['TestFieldType'])
        content = click.prompt('Enter content')
        options = self.options_manager()
        field = self.create_field(record_id, type, content, options)
        if menu_return :
            self.menu()
        else :
            return field.id
        
    # SELECT 

    def select_bucket_cli(self) :
        buckets_details = self.get_dicts_from_objects(self.buckets.values())
        bucket_fields = ['_bucket_id', '_embargo_date', '_created', '_owner']
        bucket = command_with_options('select bucket', buckets_details, True, bucket_fields)
        return bucket['_bucket_id']
    
    def select_record_cli(self, bucket_id) :
        filtered_records = [record.__dict__ for record in self.records.values() if record.bucket_id == bucket_id]
        # record_details = self.get_dicts_from_objects(record_fields)
        record_fields = ['_id', '_schema_type', '_created', '_owner']
        record = command_with_options('select record', filtered_records, True, record_fields)
        return record['_id']

    # PRINT

    def printer_cli(self, data) :
        if data == 'Bucket' :
            buckets_details = self.get_dicts_from_objects(self.buckets.values())
            pretty_print(buckets_details)
            self.menu()
        if data == 'Record' :
            records_details = self.get_dicts_from_objects(self.records.values())
            pretty_print(records_details)
            self.menu()
        if data == 'Field' :
            fields_details = self.get_dicts_from_objects(self.fields.values())
            pretty_print(fields_details)
            self.menu()

    # MISC 

    def get_dicts_from_objects(self, objects):
        return [obj.__dict__ for obj in objects]
    

    def options_manager(self, options={}):
        if click.confirm('Would you like to add an option key-value?'):
            key = click.prompt('Enter Key Name')
            value = click.prompt(f'Enter Value for {key}')
            options[key] = value
            return self.options_manager(options)
        else:
            return options
    