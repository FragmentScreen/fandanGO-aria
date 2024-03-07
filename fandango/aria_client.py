from .oauth import OAuth
from .client import Client
from .data_manager import DataManager
from .visit import Visit
from .data_manager import DataManager
class AriaClient :
    '''
    Super class. New instances initiated in the `commands`. All functionality will start with one of these methods.
    '''
    def __init__(self, login=False):
        self.client = Client(OAuth())
        if not login:
            self._fetch_token()
            # self._get_classes()

    @property
    def token(self):
        if not self._token:
            self._fetch_token()
        return self._token

    # def _get_classes(self) :
    #     self.data_manager = DataManager(self.token)
    #     self.visit_manager = Visit(self.token)
        
    def login(self, username, password):
        self.client.authenticate(username, password)

    def new_data_manager(self, bucket_id=None):
        return (DataManager(self.token, bucket_id))

    def get_access_token(self):
        return self.client.get_access_token()

    def create_bucket(self, fields=None):
        self.data_manager.create_bucket(fields)

    def list_buckets(self) :
        self.data_manager.list_buckets()

    def create_record(self) :
        self.data_manager.create_record()

    def list_records(self) :
        self.data_manager.list_records()

    def create_field(self) :
        self.data_manager.create_field()

    def list_fields(self):
        self.data_manager.list_fields()

    def get_visits(self, vid=None) : 
        visits = self.visit_manager.get_visits(vid)
        if len(visits) < 1 :
            print('No records with that ID for this facilty')
        else :
            print(visits)

    def _fetch_token(self):
        token = self.get_access_token()
        self._token = token['access_token']