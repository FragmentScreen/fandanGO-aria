import os
import unittest
from dotenv import load_dotenv
from fGOaria.classes.oauth import OAuth
from fGOaria.classes.aria_rest import AriaRest

class AriaFileUploadCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        load_dotenv()
        self.test_local_file_name = 'test_file.txt'

        self.oauth = OAuth()
        self.oauth.login(os.getenv('ARIA_CONNECTION_USERNAME'), os.getenv('ARIA_CONNECTION_PASSWORD'))

        self.aria = AriaRest(self.oauth.get_access_token())


    def testUploadFile(self):
        return_json = self.aria.upload(self.test_local_file_name, "text/plain")
        print(return_json)
        self.assertIsNotNone(return_json, "Upload did not return any data")
        self.assertIsInstance(return_json, dict, "Return data is not a valid JSON object")

        files = return_json.get('files')
        self.assertIsNotNone(files, "Return data does not contain files data")
        self.assertIsInstance(files, list, "Return data files is not a list")
        self.assertGreater(len(files), 0, "Return data files array is empty")
        file_name = files[0].get('name')
        self.assertIsNotNone(file_name, "Return file object does not contain 'name'")
        self.assertIsInstance(file_name, str, "File name is not a string")
        self.assertNotEqual(file_name, '', "File name is empty")


if __name__ == '__main__':
    unittest.main()
