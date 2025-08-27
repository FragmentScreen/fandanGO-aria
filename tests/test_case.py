import os
import unittest

RUN_INTEGRATION = os.getenv("ARIA_RUN_TESTS") == "1"

class UnitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not RUN_INTEGRATION:
            raise unittest.SkipTest("Integration tests disabled. Set ARIA_RUN_TESTS=1 to run.")
