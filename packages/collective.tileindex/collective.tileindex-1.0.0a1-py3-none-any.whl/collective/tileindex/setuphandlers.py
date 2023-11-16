from .upgrades import add_indexes
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.tileindex:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide package from site-creation and quickinstaller."""
        return []


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    add_indexes(context)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
