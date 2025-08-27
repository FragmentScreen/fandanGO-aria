import os
import unittest
from dotenv import load_dotenv
from tests.test_case import UnitTestCase
from fGOaria.classes.client_provider import ProviderClient
from fGOaria.classes.storage_manager import StorageManager
from fGOaria.classes.storage_provider import StorageProvider

class StorageClientTestCase(UnitTestCase):
    def setUp(self):
        load_dotenv()
        self.aria_password_default = os.getenv('ARIA_CONNECTION_PASSWORD')
        self.aria_email_default = os.getenv('ARIA_CONNECTION_USERNAME')
        self.test_provider = os.getenv('TEST_PROVIDER_CLIENT')
        self.test_provider_client = f"{self.test_provider}Client"
        self.test_provider_endpoint = os.getenv("TEST_PROVIDER_HOST_ENDPOINT")
        self.test_provider_token = os.getenv("TEST_PROVIDER_TOKEN")
        self.test_space_identifier_name = os.getenv('TEST_DATA_SPACE_IDENTIFIER_NAME')
        self.test_space_id = os.getenv('TEST_PROVIDER_DATA_SPACE_ID')
        self.storage = StorageManager(None, '1', 'proposal')

    def testGetProviders(self):
        """Test retrieving storage providers"""
        self.assertIsNotNone(self.storage.providers, "Providers not set")
        self.assertIsInstance(self.storage.providers, dict, "GetProviders did not return a dict")
        self.assertIsNotNone(self.storage.providers.get(self.test_provider_client),
                             f"{self.test_provider_client} not found")
        self.assertIsInstance(self.storage.providers.get(self.test_provider_client), StorageProvider,
                              "StorageProvider obj not found")

    def testOption(self):
        print("test opt", self.storage.providers.keys())
        clients = list(self.storage.providers.keys())
        self.assertEqual(clients[0], self.test_provider_client, f"Couldn't find {self.test_provider_client}")

    def testSelect(self):
        client = self.storage.select(self.test_provider_client)
        self.assertIsInstance(client, ProviderClient, "Select did not return a ProviderClient")
        self.assertEqual(client.__class__.__name__, self.test_provider_client,
                         f"Select did not return a {self.test_provider_client}")

    def testConnection(self):
        client = self.storage.select(self.test_provider_client)
        self.assertIsNotNone(client.data_space(), "Could not get space details")
        self.assertIsNotNone(client.data_space().keys().__contains__(self.test_space_identifier_name),
                             "Could not retrieve space details")
        self.assertIsNotNone(client.data_space()[self.test_space_identifier_name],
                             "Could not get any space ID")
        self.assertEqual(client.data_space()[self.test_space_identifier_name], self.test_space_id,
                             "Could not find data space")

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
