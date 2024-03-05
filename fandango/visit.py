from .config import *
from .utils import *
import yaml

root_project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
config_path = os.path.join(root_project_dir, "config.yml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

class Visit:
    '''
    Class for managing visit data retrieved from the ARIA Visit API.
    The env. Visit_url must be set, including your facility ID. See docs.
    '''
    def __init__(self, token):
        self.token = token
        self.rest_server = config["login"]["VISIT_URL"]

    def get_visits(self, vid):
        if not self.token:
            logging.info('Error: Token not loaded')
            return
        if vid:
            self.add_filter('id', vid)

        headers = {'Authorization': f'Bearer {self.token}'}
        req = requests.get(self.rest_server, headers=headers)
        req.raise_for_status()
        return req.json()['data']['items']
    
    def add_filter(self, key, value) : 
        self.rest_server = self.rest_server + f'&filter[{key}]={value}'