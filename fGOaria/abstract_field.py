from abc import ABC, abstractmethod

class AbstractField(ABC):
    @property
    @abstractmethod
    def record_id(self):
        """Getter for the Record ID."""
        pass

    @record_id.setter
    @abstractmethod
    def record_id(self, value):
        """Setter for the Record ID."""
        pass

    @property
    @abstractmethod
    def field_type(self):
        """Getter for the Field Type."""
        pass

    @field_type.setter
    @abstractmethod
    def field_type(self, value):
        """Setter for the Field Type."""
        pass

    @property
    @abstractmethod
    def content(self):
        """Getter for the Field Content."""
        pass

    @content.setter
    @abstractmethod
    def content(self, value):
        """Setter for the Field Content."""
        pass

    @property
    @abstractmethod
    def options(self):
        """Getter for the Field Options"""
        pass

    @options.setter
    @abstractmethod
    def options(self, value):
        """Setter for the Field Options"""
        pass