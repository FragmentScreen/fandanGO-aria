from .oauth import OAuth
from .client import Client
from .do_something import DoSomething

class AriaClient :
    '''
    Super class. New instances initiated in the `commands`. All functionality will start with one of these methods.
    '''
    def __init__(self) :
        self.client = Client(OAuth())

    def login(self, username, password):
        self.client.authenticate(username, password)

    def get_access_token(self) : 
        return self.client.get_access_token()
    
    def do_something(self) : 
        token = self.get_access_token()
        DoSomething.dispatch_hook(token)
