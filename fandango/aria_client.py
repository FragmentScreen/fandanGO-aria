from .oauth import OAuth
from .client import Client
from .data_manager import DataManager
from .bucket import Bucket
from .visit import Visit
from .data_manager import DataManager
from .cli_data_manager import DataManagerCLI
class AriaClient :
    '''
    Super class. New instances initiated in the `commands`. All functionality will start with one of these methods.
    '''
    def __init__(self, login=False):
        self.client = Client(OAuth())
        if not login:
            self._fetch_token()

    @property
    def token(self):
        if not self._token:
            self._fetch_token()
        return self._token
        
    def login(self, username, password):
        self.client.authenticate(username, password)

    def new_data_manager(self, id, type, populate=False):
        return (DataManager(self.token, id, type, populate))
    
    def new_cli_manager(self, id, type, populate=False) :
        return (DataManagerCLI(self.token, id, type, populate))

    def new_data_managers(self, entities=None):
        if entities is None:
            entities = {}

        data_managers = {}
        for key, value in entities.items():
            data_managers[f'data_manager_{key}_{value}'] = DataManager(self.token, key, value, True)
        return data_managers
    
    def get_access_token(self):
        return self.client.get_access_token()

    def get_visits(self, vid=None) : 
        visits = self.visit_manager.get_visits(vid)
        if len(visits) < 1 :
            print('No records with that ID for this facilty')
        else :
            print(visits)

    def _fetch_token(self):
        token = self.get_access_token()
        self._token = token['access_token']