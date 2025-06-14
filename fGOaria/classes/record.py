from ..utils.imports_config import *
from ..utils.utility_functions import *

class Record():
    def __init__(self, bucket_id: str, schema: str, description: str = None):
        self._bucket_id = bucket_id
        self._schema_type = schema
        self._id = None
        self._owner = None
        self._description = description
        self._created = None
        self._updated = None

    @property
    def bucket_id(self):
        """Getter for the Bucket ID."""
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, value):
        """Setter for the Bucket ID."""
        self._bucket_id = value

    @property
    def schema_type(self):
        """Getter for the Schema Type."""
        return self._schema_type

    @schema_type.setter
    def schema_type(self, value):
        """Setter for the Schema Type."""
        self._schema_type = value

    @property
    def id(self):
        """Getter for the Record ID."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for the Record ID."""
        self._id = value

    @property
    def owner(self):
        """Getter for the Record owner."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """Setter for the Record owner."""
        self._owner = value

    @property
    def created(self):
        """Getter for the Record created timestamp."""
        return self._created

    @created.setter
    def created(self, value):
        """Setter for the Record created timestamp."""
        self._created = value

    @property
    def updated(self):
        """Getter for the Record updated timestamp."""
        return self._updated

    @updated.setter
    def updated(self, value):
        """Setter for the Record updated timestamp."""
        self._updated = value

    @property
    def description(self):
        """Getter for the Record description."""
        return self._description
    
    @description.setter
    def description(self, value):
        """Setter for the Record description."""

    def populate(self, data):
        """Populate record with additional properties."""
        self._id = data.get('id')
        self._owner = data.get('owner')
        self._created = data.get('created')
        self._updated = data.get('updated')