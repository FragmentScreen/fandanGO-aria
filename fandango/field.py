from .utils import *
from .imports_config import *
from .abstract_field import AbstractField

class Field(AbstractField) :
    def __init__(self, record_id: str, field_type : str, content : str, options : dict = None, order: int = 0, **kwargs):
        self._record_id = record_id
        self._field_type = field_type
        self._content = content
        self._options = options if options is not None else {}
        self._order = order
        self._id = kwargs.get('id')
        

    @property
    def record_id(self):
        """Getter for the Field's Record ID."""
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        """Setter for the Field's Record ID."""
        self._record_id = value

    @property
    def field_type(self):
        """Getter for the Field Type."""
        return self._field_type

    @field_type.setter
    def field_type(self, value):
        """Setter for the Field Type."""
        self._field_type = value

    @property
    def content(self):
        """Getter for the Field Content."""
        return self._content

    @content.setter
    def content(self, value):
        """Setter for the Field Content."""
        self._content = value

    @property
    def options(self):
        """Getter for the Field Options."""
        return self._options

    @options.setter
    def options(self, value):
        """Setter for the Field Options."""
        self._options = value

    @property
    def order(self):
        """Getter for the Field Order."""
        return self._order

    @order.setter
    def order(self, value):
        """Setter for the Field Order."""
        self._order = value
    
    @property
    def id(self):
        """Getter for the Field ID."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for the Field ID."""
        self._id = value

    def populate(self, data):
        """Populate field with additional properties after pushing to the database."""
        self._id = data.get('id')


        