from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import collective.tileindex


class CollectiveTileindexLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.tileindex)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.tileindex:default")


COLLECTIVE_TILEINDEX_FIXTURE = CollectiveTileindexLayer()


COLLECTIVE_TILEINDEX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_TILEINDEX_FIXTURE,),
    name="CollectiveTileindexLayer:IntegrationTesting",
)


COLLECTIVE_TILEINDEX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_TILEINDEX_FIXTURE,),
    name="CollectiveTileindexLayer:FunctionalTesting",
)
