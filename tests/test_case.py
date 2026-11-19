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

        from pathlib import Path
        from tempfile import TemporaryDirectory

        token_dir = TemporaryDirectory()
        cls.addClassCleanup(token_dir.cleanup)
        for target in (
            'fGOaria.classes.oauth.Path',
            'fGOaria.utils.encryption.Path',
        ):
            path_patch = patch(target, wraps=Path)
            isolated_path = path_patch.start()
            cls.addClassCleanup(path_patch.stop)
            isolated_path.home.return_value = Path(token_dir.name)

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