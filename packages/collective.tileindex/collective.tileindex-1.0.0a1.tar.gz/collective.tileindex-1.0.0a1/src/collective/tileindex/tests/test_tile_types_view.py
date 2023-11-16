from collective.tileindex.testing import COLLECTIVE_TILEINDEX_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter

import unittest


class ViewsIntegrationTest(unittest.TestCase):
    layer = COLLECTIVE_TILEINDEX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_tile_types_is_registered_document(self):
        api.content.create(self.portal, "Document", "front-page")
        view = getMultiAdapter(
            (self.portal["front-page"], self.portal.REQUEST), name="tile-types-view"
        )
        self.assertIsNone(view.tile_types)

    def test_tile_types_is_registered_folder(self):
        api.content.create(self.portal, "Folder", "other-folder")
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST), name="tile-types-view"
        )
        self.assertIsNone(view.tile_types)
