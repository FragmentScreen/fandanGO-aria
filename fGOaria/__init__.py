import core  # type: ignore
from .bucket import Bucket
from .record import Record
from .aria_client import AriaClient
from .field import Field
from .utils import *
from .visit import Visit
from .entity_manager import EntityManager
from fGOaria.actions import deposit_field
from fGOaria.constants import ACTION_DEPOSIT_FIELD


class Plugin(core.Plugin) : 

    @classmethod
    def define_methods(cls) : 
        cls.define_method(ACTION_DEPOSIT_FIELD, deposit_field.perform_action)
