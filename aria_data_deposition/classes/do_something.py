class DoSomething :
    '''
    Demo class for testing encapsulation of Oauth/Client
    '''
    def __init__(self) :
        self.random = 'blah'

    def dispatch_hook(token) :
        if token :
            tokenf=token['expires_in']
            print(f'token in dispatcher. {tokenf}')