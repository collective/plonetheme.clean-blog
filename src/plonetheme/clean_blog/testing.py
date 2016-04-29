# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.clean_blog


class PlonethemeCleanBlogLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.clean_blog)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.clean_blog:default')


PLONETHEME_CLEANBLOG_FIXTURE = PlonethemeClean-BlogLayer()


PLONETHEME_CLEANBLOG_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_CLEANBLOG_FIXTURE,),
    name='PlonethemeClean-BlogLayer:IntegrationTesting'
)


PLONETHEME_CLEANBLOG_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_CLEANBLOG_FIXTURE,),
    name='PlonethemeClean-BlogLayer:FunctionalTesting'
)


PLONETHEME_CLEANBLOG_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_CLEANBLOG_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeClean-BlogLayer:AcceptanceTesting'
)
