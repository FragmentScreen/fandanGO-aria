import os
import unittest
from unittest.mock import patch

from dotenv import load_dotenv

load_dotenv()
RUN_TESTS = os.getenv("ARIA_RUN_TESTS") == "1"

class UnitTestCase(unittest.TestCase):
    requires_live_aria = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if not cls.requires_live_aria:
            return
        if not RUN_TESTS:
            raise unittest.SkipTest("Tests disabled. Set ARIA_RUN_TESTS=1 in your environment to run.")

        required = (
            'ARIA_CONNECTION_USERNAME', 'ARIA_CONNECTION_PASSWORD',
            'ARIA_CONNECTION_LOGIN_URL_LOCAL' if os.getenv('DEV', 'LOCAL') == 'LOCAL' else 'ARIA_CONNECTION_LOGIN_URL',
            'ARIA_CONNECTION_GRANT_TYPE',
            'ARIA_CONNECTION_SCOPE', 'ARIA_CLIENT_ID', 'ARIA_CLIENT_SECRET',
        )
        missing = [name for name in required if not os.getenv(name)]
        if missing:
            raise ValueError("Missing live test configuration: " + ", ".join(missing))

        cls.aria_credentials = {
            "username": os.getenv('ARIA_CONNECTION_USERNAME'),
            "password": os.getenv('ARIA_CONNECTION_PASSWORD'),
            "use_keyring": False
        }

    # def setUp(self):
    #     super().setUp()
    #     if not self.requires_live_aria:
    #         network_guard = patch(
    #             "requests.sessions.Session.request",
    #             side_effect=AssertionError("Offline tests must not make HTTP requests"),
    #         )
    #         network_guard.start()
    #         self.addCleanup(network_guard.stop)