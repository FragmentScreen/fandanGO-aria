from .oauth import OAuth
from .data_manager import DataManager
from .bucket import Bucket
from .visit import Visit
from .data_manager import DataManager
from .cli_data_manager import DataManagerCLI
from .token import Token
from .entity_manager import EntityManager
class AriaClient :
    '''
    Super class. New instances initiated in the `commands`. All functionality will start with one of these methods.
    '''
    def __init__(self, login=False):
        self.oauth = OAuth()
        if login:
            self.login()
        self._fetch_token()
        

    @property
    def token(self):
        if not self._token:
            self._fetch_token()
        return self._token
        
    def login(self):
        self.oauth.login()

    def new_data_manager(self, id, type, populate=False):
        return (DataManager(self.token, id, type, populate))
    
    def new_cli_manager(self, id, type, populate=False) :
        return (DataManagerCLI(self.token, id, type, populate))
    
    def new_entity_manager(self) :
        return (EntityManager(self.token))

    def new_data_managers(self, entities=None):
        if entities is None:
            entities = {}

        data_managers = {}
        for key, value in entities.items():
            data_managers[f'data_manager_{key}_{value}'] = DataManager(self.token, key, value, True)
        return data_managers
    
    def get_access_token(self):
        return self.oauth.get_access_token()

    def _fetch_token(self):
        token : Token = self.get_access_token()
        self._token = token.access_token