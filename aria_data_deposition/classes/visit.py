from ..config import *
from ..utils import *

load_dotenv('.env')

class Visit:
    '''
    Class for managing visit data retrieved from the ARIA Visit API.
    The env. Visit_url must be set, including your facility ID. See docs.
    '''
    def __init__(self):
        self.rest_server = os.getenv('VISIT_URL')

    def get_visits(self, token, vid):
        if not token:
            logging.info('Error: Token not loaded')
            return
        if vid:
            self.add_filter('id', vid)

        token = token['access_token']
        headers = {'Authorization': f'Bearer {token}'}
        req = requests.get(self.rest_server, headers=headers)
        req.raise_for_status()
        return req.json()['data']['items']
    
    def add_filter(self, key, value) : 
        self.rest_server = self.rest_server + f'&filter[{key}]={value}'