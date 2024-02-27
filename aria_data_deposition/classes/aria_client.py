from .oauth import OAuth
from .client import Client
from .do_something import DoSomething
from .data_manager import DataManager
class AriaClient :
    '''
    Super class. New instances initiated in the `commands`. All functionality will start with one of these methods.
    '''
    def __init__(self, login=False):
        self.client = Client(OAuth())
        self.data_manager = DataManager()
        if not login:
            self._fetch_token()

    @property
    def token(self):
        if not self._token:
            self._fetch_token()
        return self._token

    def _fetch_token(self):
        self._token = self.client.get_access_token()['access_token']

    def login(self, username, password):
        self.client.authenticate(username, password)

    def get_access_token(self):
        return self.client.get_access_token()

    def do_something(self):
        DoSomething.dispatch_hook(self.token)

    def create_bucket(self):
        self.data_manager.create_bucket(self.token)

    def list_buckets(self) :
        self.data_manager.list_buckets(self.token)

    def create_record(self) :
        self.data_manager.create_record(self.token)

    def list_records(self) :
        self.data_manager.list_records(self.token)

    def create_field(self) :
        self.data_manager.create_field(self.token)

    def list_fields(self):
        self.data_manager.list_fields(self.token)