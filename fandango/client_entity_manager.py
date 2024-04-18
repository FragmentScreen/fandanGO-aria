from .field import Field
from .bucket import Bucket
from .record import Record
from .api_client import APIClient
from .imports_config import *
from .utils import get_config

config = get_config()
class EntityManagerClient(APIClient):
    def __init__(self, token):
        super().__init__(token)
        self.token = token
        self.facility = config['FACILITY']['ID']
        self.visits_url = config["ENDPOINTS"]['GET']["VISITS"]
        self.proposal_data_url = config['ENDPOINTS']['GET']['PROPOSAL_DATA']
        self.proposal_url = config['ENDPOINTS']['GET']['PROPOSAL']

        self.load_url()

    def load_url(self) :
        dev = config.get('DEV', 'LOCAL')
        self.base_url = config['API'][dev]['ENTITY_BASE']

        
    def pull_fac_visits(self, vid : int = None) -> Union[dict, list] :
        data = {
            'cid' : [self.facility],
            'id' : vid if vid else None
        }
        response = self.get(self.visits_url, data)
        visits = response['data']['items']
        return visits
    
    def pull_proposal_data(self, pid) -> Union[dict, list] :
        data = {
            'pid' : pid
        }
        try :
            response = self.get(self.proposal_data_url, data)
            proposal_data = response['data']['items']
            return proposal_data
        except :
            raise ValueError('Proposal cannot be located')


        
    def pull_proposal(self, pid) -> Union[dict, list] :
        try :
            response = self.get(f'{self.proposal_url}{pid}')
            proposal = response['data']['items'][0]
            return proposal
        except :
            logging.error(' Proposal cannot be located.')
