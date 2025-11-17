import os
import unittest
import json
from dotenv import load_dotenv
from tests.test_case import UnitTestCase
from fGOaria.classes import storage_manager
from fGOaria.classes.client_provider import ProviderClient
from fGOaria.classes.storage_provider import StorageProvider
from fGOaria.classes.oauth import OAuth
from fGOaria.classes.credentials import Credentials
from fGOaria.classes.token import Token

class StorageProvisioningTestCase(UnitTestCase):
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
        #self.test_file_id= '000000000052F37A67756964233137316637656564363634623164636163653737323064623363376464386134636864366463233935336136643135373835313830316462646634316262653163333434366639636864366463'
        self.test_file_name = 'test_file3.txt'

        self.oauth = OAuth()
        self.oauth.login(os.getenv('ARIA_CONNECTION_USERNAME'), os.getenv('ARIA_CONNECTION_PASSWORD'))

        self.storage = storage_manager.StorageManager(self.oauth.get_access_token().access_token,
                                                      os.getenv('TEST_VISIT_ID'))

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

    def testGetProviders(self):
        self.assertIsNotNone(self.storage.providers, "Providers not set")
        self.assertIsInstance(self.storage.providers, dict, "GetProviders did not return a dict")
        self.assertIsNotNone(self.storage.providers.get(self.test_provider_id),
                             f"{self.test_provider_client} not found")
        self.assertIsInstance(self.storage.providers.get(self.test_provider_id), StorageProvider,
                              "StorageProvider obj not found")

    def testProviderOptions(self):
        valid_provider_types = [p for p in storage_manager.PROVIDER_CLIENT_MAP.keys()]
        for provider in self.storage.providers.values():
            self.assertIn(provider.type, valid_provider_types,
                          f"Couldn't find {provider.type} in valid provider types list")

    def testSelectOption(self):
        self.storage.select(self.test_provider_id)
        self.assertIsNotNone(self.storage.selected, "No storage provider selected")
        self.assertIsInstance(self.storage.selected, StorageProvider,
                              "Selected storage provider is not a StorageProvider")

    def testProvisionOption(self):
        self.storage.select(self.test_provider_id)
        self.storage.provision()
        self.assertIsInstance(self.storage.client, ProviderClient,
                              "Provisioning did not set up a ProviderClient")
        self.assertEqual(self.storage.client.__class__.__name__, self.test_provider_client,
                         f"Provisioning {self.storage.client.__class__.__name__} did not set up a {self.test_provider_client}")

    # def testConnection(self):
    #     self.storage.select(self.test_provider_id)
    #     self.storage.provision()
    #     self.assertIsNotNone(self.storage.client.data_space(), "Could not get space details")
    #     self.assertIsNotNone(self.storage.client.data_space,
    #                          "Could not retrieve space details")
    #     self.assertIsNotNone(self.storage.client.data_space()[self.test_space_identifier_name],
    #                          "Could not get any space ID")
    #     self.assertEqual(self.storage.client.data_space()[self.test_space_identifier_name], self.test_space_id,
    #                      "Could not find data space")

    def testUploadFile(self):
        """@todo"""
        pass
        # self.storage.select(self.test_provider_id)
        # self.storage.provision()

        # return_json = self.storage.client.upload(self.test_file_name)
        # self.assertIsNotNone(return_json, "Upload did not return any data")
        # self.assertIsInstance(return_json, dict, "Return data is not a valid JSON object")
        # self.assertIn(self.test_provider_file_id_name, return_json.keys(), "Return data does not contain file ID")

        # file_id = return_json.get(self.test_provider_file_id_name)
        # self.assertIsNotNone(file_id,  "Return data does not contain file ID data")
        # self.assertIsInstance(file_id, str, "Return data file ID is not a string")
        # self.assertNotEqual(file_id, '', "Return data did not return a file ID")

    def testFindLocationFile(self):
        """@todo"""
        # self.file_id or self.location = self.storage.select('OneDataClient').locate('thing')
        pass

    def testDownloadFile(self):
        self.storage.select(self.test_provider_id)
        self.storage.provision()

        file_id = self.storage.client.locate(self.test_file_name)

         # Define a destination path (e.g. local Downloads folder)
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        os.makedirs(downloads_dir, exist_ok=True)
        dest_path = os.path.join(downloads_dir, self.test_file_name)
        
        # file_info = self.storage.client.locate(self.test_file_name)

        print(f"File info in OneData: {dest_path}")

        try:
            downloaded_path = self.storage.client.download(file_id, dest_path)
        except Exception as e:
            self.fail(f"Download failed with exception: {e}")

    # Confirm file exists and has size > 0
    #     assert os.path.exists(downloaded_path), f"File not found at {downloaded_path}"
      #   assert os.path.getsize(downloaded_path) > 0, f"Downloaded file is empty: {downloaded_path}"


    def testDeleteFile(self):
        """@todo"""
        # self.storage.select('OneDataClient').delete('thing', self.file_id)
        pass


if __name__ == '__main__':
    unittest.main()
