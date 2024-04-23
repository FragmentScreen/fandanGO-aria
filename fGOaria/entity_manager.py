from .imports_config import *
from .utils import *
from .visit import Visit
from .client_entity_manager import EntityManagerClient as EntityClient

class EntityManager():
    '''
    Class for managing ARIA entity data.
    Config URLs must be set, including your facility ID. See docs.
    '''
    def __init__(self, token):
        self.client = EntityClient(token)
        self.visits = {}
        self.proposals = {}

    def get_fac_visits(self, vid=None):
        visits = self.client.pull_fac_visits(vid)
        for visit in visits :
            new_visit = Visit(visit)
            id = int(new_visit._id)
            self.visits[id] = new_visit

    def get_proposal_data(self, pid) :
        proposal_data = self.client.pull_proposal_data(pid)
        if proposal_data :
            return proposal_data

    def get_proposal(self, pid) :
        proposal = self.client.pull_proposal(pid)
        if proposal :
            return proposal
    