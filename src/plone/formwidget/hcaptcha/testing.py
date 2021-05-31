# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import plone.formwidget.hcaptcha


class PloneFormwidgetHcaptchaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plone.formwidget.hcaptcha)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.formwidget.hcaptcha:default')


PLONE_FORMWIDGET_HCAPTCHA_FIXTURE = PloneFormwidgetHcaptchaLayer()


PLONE_FORMWIDGET_HCAPTCHA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_FORMWIDGET_HCAPTCHA_FIXTURE,),
    name='PloneFormwidgetHcaptchaLayer:IntegrationTesting',
)


PLONE_FORMWIDGET_HCAPTCHA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_FORMWIDGET_HCAPTCHA_FIXTURE,),
    name='PloneFormwidgetHcaptchaLayer:FunctionalTesting',
)


PLONE_FORMWIDGET_HCAPTCHA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_FORMWIDGET_HCAPTCHA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PloneFormwidgetHcaptchaLayer:AcceptanceTesting',
)
