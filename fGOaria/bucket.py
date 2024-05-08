from .imports_config import *
from .utils import *
from .abstract_bucket import AbstractBucket

class Bucket(AbstractBucket):
    def __init__(self, entity_id : int, entity_type : str, embargo_date : str, **kwargs):
        self._entity_type = entity_type
        self._entity_id = entity_id
        self._embargo_date = embargo_date
        self._id = kwargs.get('id')
        self._owner = kwargs.get('owner')
        self._created = kwargs.get('created')
        self._updated = kwargs.get('updated')

    @property
    def entity_type(self):
        """Getter for the entity type."""
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        """Setter for the entity type."""
        self._entity_type = value

    @property
    def entity_id(self):
        """Getter for the entity ID."""
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        """Setter for the entity ID."""
        self._entity_id = value

    @property
    def embargo_date(self):
        """Getter for the embargo date."""
        return self._embargo_date

    @embargo_date.setter
    def embargo_date(self, value):
        """Setter for the embargo date."""
        self._embargo_date = value

    @property
    def id(self):
        """Getter for the Bucket ID."""
        return self._id
    
    @id.setter
    def id(self, value):
        """Setter for the Bucket ID."""
        self._id = value    
    
    @property
    def owner(self):
        """Getter for the owner."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """Setter for the owner."""
        self._owner = value

    @property
    def created(self):
        """Getter for the Created Date"""
        return self._created

    @created.setter
    def created(self, value):
        """Setter for the created date."""
        self._created = value

    @property
    def updated(self):
        """Getter for the updated date."""
        return self._updated

    @updated.setter
    def updated(self, value):
        """Setter for the updated date."""
        self._updated = value

    def populate(self,data):
        """Generate additional properties like bucket ID, owner, created, and updated."""
        self.id = data['id']
        self.owner = data['owner']
        self.created = data['created']
        self.updated = data['updated']
