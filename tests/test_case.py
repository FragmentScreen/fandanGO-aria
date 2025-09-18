import os
import unittest

RUN_TESTS = os.getenv("ARIA_RUN_TESTS") == "1"

class UnitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not RUN_TESTS:
            raise unittest.SkipTest("Tests disabled. Set ARIA_RUN_TESTS=1 in your environment to run.")
