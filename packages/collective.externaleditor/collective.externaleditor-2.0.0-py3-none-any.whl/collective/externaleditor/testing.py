from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneSandboxLayer

import collective.externaleditor


class CollectiveExternaleditorLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.externaleditor)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.externaleditor:default")


COLLECTIVE_EXTERNALEDITOR_FIXTURE = CollectiveExternaleditorLayer()


COLLECTIVE_EXTERNALEDITOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_EXTERNALEDITOR_FIXTURE,),
    name="CollectiveExternaleditorLayer:FunctionalTesting",
)
