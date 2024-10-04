from ..utils.imports_config import *
from ..utils.utility_functions import *
class Visit:
    def __init__(self, data):
        required_fields = ['id', 'proposal_id', 'access_id']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        self._id = data.get('id')
        self._pid = data.get('pid')
        self._plid = data.get('plid')
        self._status = data.get('status')
        self._acid = data.get('access_id')
        self._order = data.get('order')
        self._confirmed = data.get('confirmed')
        self._completed = data.get('completed')
        self._cancelled = data.get('cancelled')
        self._detail = data.get('detail')
        self._tech_eval_positive = data.get('tech_eval_positive')
        self._call_id = data.get('call_id')
        self._suspension_count = data.get('suspension_count')
        self._approved = data.get('approved')
        self._proposal_id = data.get('proposal_id')
        self._center_ids = data.get('center_ids')
        self._cid = data.get('cid')

    