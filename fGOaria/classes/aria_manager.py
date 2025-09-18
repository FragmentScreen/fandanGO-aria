from fGOaria.classes.storage_manager import StorageManager
from fGOaria.classes.oauth import OAuth
from fGOaria.classes.data_manager import DataManager
from fGOaria.classes.cli_techeval import TechEvalCLI
from fGOaria.classes.cli_data_manager import DataManagerCLI
from fGOaria.classes.token import Token

class ARIA:
    """
    Main interface for ARIA APIs
    @deprecated Matter of opinion, but I don't see what purpose this serves other than as another layer of abstraction
    """

    def __init__(self, login=False,):
        self.oauth = OAuth()
        if not login:
            self._fetch_token()
        
    @property
    def token(self):
        if not self._token:
            self._fetch_token()
        return self._token
        
    def login(self, username = None, password = None):
        self.oauth.login(username, password)
        self._fetch_token()

    def new_data_manager(self, id, type, populate=False):
        return (DataManager(self.token, id, type, populate))
    
    def new_cli_data_manager(self, id, type, populate=False) :
        return (DataManagerCLI(self.token, id, type, populate))

    def new_storage_manager(self, id, type):
        return (StorageManager(self.token, id, type))

    def new_cli_tech_eval(self) :
        return (TechEvalCLI(self.token))

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