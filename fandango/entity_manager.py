from .config import *
from .utils import *
from .visit import Visit
from .client_entity_manager import EntityManagerClient as EntityClient
config = get_config()

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
            print(id)
            self.visits[id] = new_visit
            print(new_visit.__dict__)

    def get_proposal_data(self, pid) :
        proposal_data = self.client.pull_proposal_data(pid)
        pretty_print(proposal_data)

    def get_proposal(self, pid) :
        proposal = self.client.pull_proposal(pid)
        if proposal :
            pretty_print(proposal)
    