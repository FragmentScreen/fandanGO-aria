from abc import ABC, abstractmethod

class AbstractRecord(ABC):
    @property
    @abstractmethod
    def bucket_id(self):
        """Abstract property for the Bucket ID."""
        pass

    @bucket_id.setter
    @abstractmethod
    def bucket_id(self, value):
        """Abstract setter for the Bucket ID."""
        pass

    @property
    @abstractmethod
    def schema_type(self):
        """Abstract property for the Schema Type."""
        pass

    @schema_type.setter
    @abstractmethod
    def schema_type(self, value):
        """Abstract setter for the Schema Type.."""
        pass
