from .data_manager import DataManager
from .utils import *
from .imports_config import Union
import click


class DataManagerCLI(DataManager):
    def __init__(self, token, entity_id, entity_type, populate):
        """
        Initialize DataManagerCLI instance.

        :param token: Token for authentication.
        :param entity_id: Entity ID.
        :param entity_type: Entity type.
        :param populate: Flag to indicate whether to populate data.
        """
        super().__init__(token, entity_id, entity_type, populate)

    def menu(self) -> None: 
        """
        Display the main menu and handle user input for menu navigation.
        """
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
            
    def creator_cli(self, data) -> None:
        if data == 'Bucket' :
            self.create_bucket_cli()
        if data == 'Record' :
            self.create_record_cli()
        if data == 'Field' :
            self.create_field_cli()

    def create_bucket_cli(self, menu_return=True) -> Union[str, None] :
        embargo= click.prompt('Emargoed Until (dd/mm/yy)', type=click.DateTime(formats=['%d/%m/%y']), default='', show_default=False)
        embargo = format_datetime_to_json_serializable(embargo)
        bucket = self.create_bucket(embargo)
        print_created_message(bucket)
        if menu_return :
            return self.menu()
        else:
            return bucket.id 
        
    def create_record_cli(self, menu_return=True) -> Union[str, None] :
        existing_bucket = click.confirm('Create record for existing Bucket?')
        if not existing_bucket :
            bucket_id = self.create_bucket_cli(False)
        else : 
            bucket_id = self.select_bucket_cli()
        if not bucket_id :
            print(f'No buckets exist for this Entity, returning to menu.')
            return self.menu()
        schema = command_with_options('Select Schema Type', ['TestSchema', 'WrongSchema'])
        record = self.create_record(bucket_id, schema)
        print_created_message(record)
        if menu_return : 
           return self.menu()
        else :
            return record.id
    
    def create_field_cli(self) -> None:
        existing_record = click.confirm('Create field for existing Record?')
        if not existing_record :
            record_id = self.create_record_cli(False)
        else :
            print_with_spaces('Selecting bucket....')
            bucket_id = self.select_bucket_cli()
            record_id = self.select_record_cli(bucket_id)
        if not record_id : 
            print(f'No records exist for bucket {bucket_id}, returning to menu.')
            return self.menu()
        type = command_with_options('Select Field Type', ['TestFieldType'])
        content = click.prompt('Enter content')
        options = options_manager()
        field = self.create_field(record_id, type, content, options)
        print_created_message(field)
        self.menu()
        
    # SELECT 

    def select_bucket_cli(self) -> Union[str, None] :
        buckets_details = get_dicts_from_objects(self.buckets.values())
        bucket_fields = ['_id', '_embargo_date', '_created', '_owner']
        bucket = command_with_options('select bucket', buckets_details, True, bucket_fields)
        return bucket['_id']
    
    def select_record_cli(self, bucket_id : str) -> Union[str, None] :
        filtered_records = [record.__dict__ for record in self.records.values() if record.bucket_id == bucket_id]
        if not filtered_records :
            return False
        record_fields = ['_id', '_schema_type', '_created', '_owner']
        record = command_with_options('select record', filtered_records, True, record_fields)
        return record['_id']

    # PRINT

    def printer_cli(self, data) -> None:
        if data == 'Bucket' :
            object_display = get_dicts_from_objects(self.buckets.values())
        if data == 'Record' :
            object_display = get_dicts_from_objects(self.records.values())
        if data == 'Field' :
            object_display = get_dicts_from_objects(self.fields.values())

        pretty_print(object_display)


    