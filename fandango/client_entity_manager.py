from .field import Field
from .bucket import Bucket
from .record import Record
from .api_client import APIClient
from .config import *
from .utils import get_config

config = get_config()
class EntityManagerClient(APIClient):
    def __init__(self, token):
        super().__init__(token)
        self.token = token
        self.facility = config['fac']['ID']
        self.visits_url = config["apis"]["VISITS"]
        self.proposal_data_url = config['apis']['PROPOSAL_DATA']
        self.proposal_url = config['apis']['PROPOSAL']
        self.base_url = config['apis']["ENTITY_BASE"]

        
    def pull_fac_visits(self, vid : int = None) -> dict | None :
        data = {
            'cid' : self.facility,
            'id' : vid if vid else ''
        }
        response = self.get(self.visits_url, data)
        visits = response['data']['items']
        return visits
    
    def pull_proposal_data(self, pid) -> dict | None :
        data = {
            'pid' : pid
        }
        try :
            response = self.get(self.proposal_data_url, data)
            proposal_data = response['data']['items']
            return proposal_data
        except :
            raise ValueError('Proposal cannot be located')


        
    def pull_proposal(self, pid) -> dict | None :
        try :
            response = self.get(f'{self.proposal_url}{pid}')
            proposal = response['data']['items'][0]
            return proposal
        except :
            logging.error(' Proposal cannot be located.')
