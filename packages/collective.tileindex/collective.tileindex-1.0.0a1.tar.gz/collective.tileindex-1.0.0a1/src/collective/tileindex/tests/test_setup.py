"""Setup tests for this package."""
from collective.tileindex.testing import (  # noqa: E501
    COLLECTIVE_TILEINDEX_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.tileindex is properly installed."""

    layer = COLLECTIVE_TILEINDEX_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.tileindex is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.tileindex"))

    def test_browserlayer(self):
        """Test that ICollectiveTileindexLayer is registered."""
        from collective.tileindex.interfaces import ICollectiveTileindexLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveTileindexLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = COLLECTIVE_TILEINDEX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.tileindex")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.tileindex is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("collective.tileindex"))

    def test_browserlayer_removed(self):
        """Test that ICollectiveTileindexLayer is removed."""
        from collective.tileindex.interfaces import ICollectiveTileindexLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveTileindexLayer, utils.registered_layers())
