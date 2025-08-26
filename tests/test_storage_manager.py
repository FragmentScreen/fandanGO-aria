import os
import unittest
from dotenv import load_dotenv
from fGOaria.classes.client_provider import ProviderClient
from fGOaria.classes.storage_manager import StorageManager
from fGOaria.classes.storage_provider import StorageProvider

class StorageClientTestCase(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.password_default = os.getenv('ARIA_CONNECTION_PASSWORD')
        self.email_default = os.getenv('ARIA_CONNECTION_USERNAME')
        self.storage_manager = StorageManager(None, '1', 'proposal')
        self.test_provider = "OneDataClient"

    def testGetProviders(self):
        """Test retrieving storage providers"""
        self.assertIsNotNone(self.storage_manager.providers, "Providers not set")
        self.assertIsInstance(self.storage_manager.providers, dict, "GetProviders did not return a dict")
        self.assertIsNotNone(self.storage_manager.providers.get(self.test_provider), f"{self.test_provider} not found")
        self.assertIsInstance(self.storage_manager.providers.get(self.test_provider), StorageProvider, "StorageProvider obj not found")

    def testOption(self):
        print("test opt", self.storage_manager.providers.keys())
        clients = list(self.storage_manager.providers.keys())
        self.assertEqual(clients[0], self.test_provider, f"Couldn't find {self.test_provider}")

    def testSelect(self):
        client = self.storage_manager.select(self.test_provider)
        self.assertIsInstance(client, ProviderClient, "Select did not return a ProviderClient")
        self.assertIs(client.__class__.__name__, self.test_provider, f"Select did not return a {self.test_provider}")

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
