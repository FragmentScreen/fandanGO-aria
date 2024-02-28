from .oauth import OAuth
from .client import Client
from .visit import Visit
from .do_something import DoSomething
from ..utils import *

class AriaClient :
    '''
    Super class. New instances initiated in the `commands`. All functionality will start with one of these methods.
    '''
    def __init__(self) :
        self.client = Client(OAuth())
        self.token = self.get_access_token()
        self.visit_manager = Visit()

    def login(self, username, password):
        self.client.authenticate(username, password)

    def get_access_token(self) : 
        return self.client.get_access_token()
    
    def get_visits(self, vid=None) : 
        token = self.token
        visits = self.visit_manager.get_visits(token, vid)
        if len(visits) < 1 :
            print('No records with that ID for this facilty')
        else :
            print(json.dumps(visits, indent=4))
