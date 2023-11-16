from collective.tileindex.testing import COLLECTIVE_TILEINDEX_FUNCTIONAL_TESTING
from collective.tileindex.testing import COLLECTIVE_TILEINDEX_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class IndexerIntegrationTest(unittest.TestCase):
    layer = COLLECTIVE_TILEINDEX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_dummy(self):
        self.assertTrue(True)


class IndexerFunctionalTest(unittest.TestCase):
    layer = COLLECTIVE_TILEINDEX_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_dummy(self):
        self.assertTrue(True)
