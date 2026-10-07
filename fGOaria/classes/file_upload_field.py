import json
from fGOaria.classes.aria_rest import AriaRest
from fGOaria.classes.field import Field

class FileUploadField(Field) :
    def __init__(self, record_id: str, file_path : str, file_type: str=None, options : dict = None, order: int = 0, description: str = None, **kwargs):
        super().__init__(record_id, "JSON_ARIA_FILE", "", options, order, description, **kwargs)
        self._file_path = file_path
        self._file_type = file_type

    def upload(self, token: str = None) -> None:
        response = AriaRest(token).upload(self._file_path, self._file_type)
        if not response.get('files'):
            raise Exception("File upload failed. Response: " + str(response))
        self._content = json.dumps(response.get('files')[0])
