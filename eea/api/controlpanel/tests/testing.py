"""Test layer for eea.api.controlpanel."""

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile

import eea.api.controlpanel


class EeaApiControlpanelLayer(PloneSandboxLayer):
    """Test layer for eea.api.controlpanel."""

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=eea.api.controlpanel)

    def setUpPloneSite(self, portal):
        """Set up Plone site."""
        applyProfile(portal, "eea.api.controlpanel:default")


EEA_API_CONTROLPANEL_FIXTURE = EeaApiControlpanelLayer()

EEA_API_CONTROLPANEL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EEA_API_CONTROLPANEL_FIXTURE,),
    name="EeaApiControlpanelLayer:IntegrationTesting",
)
