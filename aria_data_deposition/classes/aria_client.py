from .oauth import OAuth
from .do_something import DoSomething

class AriaClient :
    def __init__(self) :
        self.oauth = OAuth()

    def login(self, username, password):
        self.oauth.login(username, password)

    def get_token(self) : 
        return self.oauth.get_access_token()
    
    def do_something(self) : 
        token = self.get_token()
        DoSomething.dispatch_hook(token)
