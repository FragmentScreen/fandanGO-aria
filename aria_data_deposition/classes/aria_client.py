from .oauth import OAuth
from .client import Client
from .do_something import DoSomething
from .bucket_manager import DataBucketManager as DataManager
class AriaClient :
    '''
    Super class. New instances initiated in the `commands`. All functionality will start with one of these methods.
    '''
    def __init__(self, login=False) :
        self.client = Client(OAuth())
        self.data_manager = DataManager()
        if login == False :
            self.token = self.client.get_access_token()

    def login(self, username, password):
        self.client.authenticate(username, password)

    def get_access_token(self) : 
        return self.client.get_access_token()
    
    def do_something(self) : 
        token = self.get_access_token()
        DoSomething.dispatch_hook(token)

    def create_bucket(self) :
        token = self.get_access_token()
        print(token)
        print('lui')
        fields = {'aria_id': 12, "aria_entity_type" : 'visit', 'embargoed_until' : '2040-02-19 12:00:00'}
        self.data_manager.create_bucket(fields, token['access_token'])

    def list_buckets(self) :
        # token = self.get_access_token()
        self.data_manager.list_buckets(self.token['access_token'])

    def create_record(self) :
        token = self.get_access_token()
        self.data_manager.create_record(token['access_token'])

    def list_records(self) :
        token =self.get_access_token()
        self.data_manager.list_records(token['access_token'])

    def create_field(self) :
        # token = self.get_access_token()
        self.data_manager.create_field(self.token['access_token'])

    def list_fields(self):
        # token = self.get_access_token()
        self.data_manager.list_fields(self.token['access_token'])