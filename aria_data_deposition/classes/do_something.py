class DoSomething :
    def __init__(self) :
        self.random = 'blah'

    @staticmethod
    def dispatch_hook(token) :
        if token :
            tokenf=token['expires_in']
            print(f'token in dispatcher {tokenf}')