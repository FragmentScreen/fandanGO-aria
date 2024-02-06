from .oauth import OAuth


class AriaClient :
    def __init__(self) :
        self.oauth = OAuth()

    def login(self, username, password):
        self.oauth.login(username, password)
