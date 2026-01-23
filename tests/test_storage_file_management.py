import os
import unittest
import json
from dotenv import load_dotenv
from tests.test_case import UnitTestCase
from fGOaria.classes import storage_manager
from fGOaria.classes.oauth import OAuth
from fGOaria.classes.credentials import Credentials
from fGOaria.classes.token import Token

class StorageFileMgmtTestCase(UnitTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        load_dotenv()
        self.test_provider = os.getenv('TEST_PROVIDER_NAME')
        self.test_provider_id = os.getenv('TEST_PROVIDER_ID')
        self.test_provider_client = os.getenv('TEST_PROVIDER_CLIENT')
        self.test_provider_engine = os.getenv("TEST_PROVIDER_ARIA_ENGINE")
        self.test_provider_endpoint = os.getenv("TEST_PROVIDER_HOST_ENDPOINT")
        self.test_provider_token = os.getenv("TEST_PROVIDER_TOKEN")
        self.test_provider_credentials_options = os.getenv('TEST_PROVIDER_OPTIONS')
        self.test_provider_file_id_name = os.getenv('TEST_PROVIDER_FILE_ID_NAME')
        self.test_local_file_name = 'test_file.txt'
        self.test_remote_file_name = 'test_file3.txt'
        self.test_file_id = os.getenv("TEST_PROVIDER_FILE_ID")

        self.oauth = OAuth()
        self.oauth.login(os.getenv('ARIA_CONNECTION_USERNAME'), os.getenv('ARIA_CONNECTION_PASSWORD'))

        self.storage = storage_manager.StorageManager(self.oauth.get_access_token().access_token,
                                                      os.getenv('TEST_VISIT_ID'))
        self.storage.select(self.test_provider_id)
        self.storage.provision()

        # self.storage._storage_client._options = {
        #     self.test_provider: StorageProvider(
        #         provider_id=self.test_provider_id,
        #         name=self.test_provider,
        #         description="",
        #         provider_type=self.test_provider_engine,
        #         credentials=Credentials(
        #             host_endpoint=self.test_provider_endpoint,
        #             token=Token({'access_token': self.test_provider_token}),
        #             options=json.loads(self.test_provider_credentials_options)
        #         )
        #     )
        # }

    def testUploadFile(self):
        return_json = self.storage.client.file_upload(self.test_local_file_name)
        self.assertIsNotNone(return_json, "Upload did not return any data")
        self.assertIsInstance(return_json, dict, "Return data is not a valid JSON object")
        self.assertIn(self.test_provider_file_id_name, return_json.keys(), "Return data does not contain file ID")

        file_id = return_json.get(self.test_provider_file_id_name)
        self.assertIsNotNone(file_id,  "Return data does not contain file ID data")
        self.assertIsInstance(file_id, str, "Return data file ID is not a string")
        self.assertNotEqual(file_id, '', "Return data did not return a file ID")

    def testGetFileID(self):
        file_id = self.storage.client.get_file_id(self.test_remote_file_name)
        self.assertIsNotNone(file_id, "File not found; no file ID returned")

    def testDownloadFile(self):
        file_id = self.storage.client.get_file_id(self.test_remote_file_name)

         # Define a destination path (e.g. local Downloads folder)
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(downloads_dir, exist_ok=True)
        dest_path = os.path.join(downloads_dir, self.test_remote_file_name)

        try:
            downloaded_path = self.storage.client.file_download(file_id, dest_path)
        except Exception as e:
            self.fail(f"Download failed with exception: {e}")

        # Confirm file exists and has size > 0
        assert os.path.exists(downloaded_path), f"File not found at {downloaded_path}"
        assert os.path.getsize(downloaded_path) > 0, f"Downloaded file is empty: {downloaded_path}"

    def testDeleteFile(self):
        # Delete the file by id (uses locate() + delete() under the hood)
        status_code = self.storage.client.file_delete(self.test_file_id)
        # Verify HTTP success
        self.assertEqual(status_code, 204, f"Expected 204 No Content, got {status_code}")


if __name__ == '__main__':
    unittest.main()
