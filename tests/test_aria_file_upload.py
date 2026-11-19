import os
import unittest
import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
from tests.test_case import UnitTestCase
from dotenv import load_dotenv
from fGOaria.classes.oauth import OAuth
from fGOaria.classes.aria_rest import AriaRest

@pytest.mark.integration
@pytest.mark.rest_integration
class AriaFileUploadCase(UnitTestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        if os.getenv('ARIA_RUN_REST_TESTS') != '1':
            raise unittest.SkipTest("Live REST tests disabled. Set ARIA_RUN_TESTS=1 and ARIA_RUN_REST_TESTS=1 to run.")
        super().setUpClass()

        rest_url = f"ARIA_REST_{os.getenv('DEV', 'LOCAL')}"
        if not os.getenv(rest_url):
            raise ValueError("Missing REST test configuration: " + rest_url)

        fixture_dir = TemporaryDirectory()
        cls.addClassCleanup(fixture_dir.cleanup)
        cls.test_local_file_name = str(Path(fixture_dir.name) / 'test_aria_upload_fixture.txt')
        with open(cls.test_local_file_name, 'w') as fixture:
            fixture.write('ARIA upload integration test')

        cls.oauth = OAuth()
        cls.oauth.login(**cls.aria_credentials)

        cls.aria = AriaRest(cls.oauth.get_access_token(use_keyring=False))


    def testUploadFile(self):
        return_json = self.aria.upload(self.test_local_file_name, "text/plain")
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
