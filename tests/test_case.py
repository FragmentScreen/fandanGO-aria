import os
import unittest

from dotenv import load_dotenv

load_dotenv()
RUN_TESTS = os.getenv("ARIA_RUN_TESTS") == "1"

class UnitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not RUN_TESTS:
            raise unittest.SkipTest("Tests disabled. Set ARIA_RUN_TESTS=1 in your environment to run.")

        cls.aria_credentials = {
            "username": os.getenv('ARIA_CONNECTION_USERNAME'),
            "password": os.getenv('ARIA_CONNECTION_PASSWORD'),
            "use_keyring": False
        }

        super().setUpClass()