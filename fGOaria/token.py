from .imports_config import datetime, timedelta

class Token:
    def __init__(self, token_data):
        self._access_token = token_data.get('access_token', None)
        self._expires_in = token_data.get('expires_in', None)
        self._refresh_expires_in = token_data.get('refresh_expires_in', None)
        self._refresh_token = token_data.get('refresh_token', None)
        self._token_type = token_data.get('token_type', None)
        self._not_before_policy = token_data.get('not-before-policy', None)
        self._session_state = token_data.get('session_state', None)
        self._scope = token_data.get('scope', None)
        self._timestamp = token_data.get('timestamp', None)

    @property
    def access_token(self):
        return self._access_token

    @property
    def expires_in(self):
        return self._expires_in

    @property
    def refresh_expires_in(self):
        return self._refresh_expires_in

    @property
    def refresh_token(self):
        return self._refresh_token

    @property
    def token_type(self):
        return self._token_type

    @property
    def not_before_policy(self):
        return self._not_before_policy

    @property
    def session_state(self):
        return self._session_state

    @property
    def scope(self):
        return self._scope
    
    @property
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    def to_dict(self):
        return {
            'access_token': self.access_token,
            'expires_in': self.expires_in,
            'refresh_expires_in': self.refresh_expires_in,
            'refresh_token': self.refresh_token,
            'token_type': self.token_type,
            'not_before_policy': self.not_before_policy,
            'session_state': self.session_state,
            'scope': self.scope,
            'timestamp': self.timestamp
        }
    
    def is_valid (self, refresh : bool = False) -> bool :
        current_time = datetime.now()
        token_timestamp = datetime.strptime(self.timestamp, '%Y-%m-%d %H:%M:%S')

        if not refresh :
            token_expiry_time = token_timestamp + timedelta(seconds=self.expires_in)
        else :
            token_expiry_time = token_timestamp + timedelta(seconds=self.refresh_expires_in)

        if current_time < token_expiry_time :
            return True
        
        return False
        

    

    
