import unittest2 as unittest
from google.appengine.ext import testbed


class BaseTests(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()

    def tearDown(self):
        self.testbed.deactivate()

    def test_failure(self):
        assert False
