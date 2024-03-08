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

    @property
    def token(self):
        if not self._token:
            self._fetch_token()
        return self._token
        
    def login(self, username, password):
        self.client.authenticate(username, password)

    def new_data_manager(self, bucket_id=None):
        return (DataManager(self.token, bucket_id))

    def new_data_managers(self, bucket_ids=None):
        if bucket_ids is None:
            bucket_ids = []

        data_managers = {}
        for bucket_id in bucket_ids:
            data_managers[f'data_manager_{bucket_id}'] = DataManager(self.token, bucket_id)
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