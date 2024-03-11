from abc import ABC, abstractmethod

class AbstractBucket(ABC):
    @property
    @abstractmethod
    def entity_type(self):
        """Abstract property for the entity type."""
        pass

    @entity_type.setter
    @abstractmethod
    def entity_type(self, value):
        """Abstract setter for the entity type."""
        pass

    @property
    @abstractmethod
    def entity_id(self):
        """Abstract property for the entity ID."""
        pass

    @entity_id.setter
    @abstractmethod
    def entity_id(self, value):
        """Abstract setter for the entity ID."""
        pass

    @property
    @abstractmethod
    def embargo_date(self):
        """Abstract property for the embargo date."""
        pass

    @embargo_date.setter
    @abstractmethod
    def embargo_date(self, value):
        """Abstract setter for the embargo date."""
        pass