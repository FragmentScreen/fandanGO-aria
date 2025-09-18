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
        self.test_file_name = 'test_file.txt'

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
        # self.storage_manager.select('OneDataClient').upload('thing')
        pass

    def testFindLocationFile(self):
        """@todo"""
        # self.file_id or self.location = self.storage_manager.select('OneDataClient').locate('thing')
        pass

    def testDownloadFile(self):
        """@todo"""
        # self.storage_manager.select('OneDataClient').download('thing', self.file_id)
        pass

    def testDeleteFile(self):
        """@todo"""
        # self.storage_manager.select('OneDataClient').delete('thing', self.file_id)
        pass


if __name__ == '__main__':
    unittest.main()
