from .bucket import Bucket
from .record import Record
from .aria_client import AriaClient
from .field import Field
from .utils import *
from .visit import Visit
from .entity_manager import EntityManager

try:
    import core # type: ignore
    from fGOaria.actions import deposit_field   
    from fGOaria.constants import ACTION_DEPOSIT_FIELD
    CORE_SOFTWARE_AVAILABLE = True
except ImportError:
    print_with_spaces('FandanGO Core not available, ARIA plugin acting independently...')
    CORE_SOFTWARE_AVAILABLE = False

if CORE_SOFTWARE_AVAILABLE:
    class Plugin(core.Plugin) : 

        @classmethod
        def define_methods(cls) : 
            cls.define_method(ACTION_DEPOSIT_FIELD, deposit_field.perform_action)
