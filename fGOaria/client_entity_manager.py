from .field import Field
from .bucket import Bucket
from .record import Record
from .api_client import APIClient
from .imports_config import *
from .utils import get_config
from dotenv import load_dotenv

load_dotenv()
class EntityManagerClient(APIClient):
    def __init__(self, token):
        super().__init__(token)
        self.token = token
        self.facility = os.getenv('ARIA_FACILITY_ID')
        self.visits_url = os.getenv('ARIA_ENTITY_VISIT_URL')
        self.proposal_data_url = os.getenv('ARIA_ENTITY_PROPOSAL_DATA_URL')
        self.proposal_url = os.getenv('ARIA_ENTITY_PULL_PROPOSAL_URL')
        self.base_url = os.getenv('ARIA_ENTITY_URL')

        
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
