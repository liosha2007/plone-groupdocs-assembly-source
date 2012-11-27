from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import groupdocs.assembly


GROUPDOCS_ASSEMBLY = PloneWithPackageLayer(
    zcml_package=groupdocs.assembly,
    zcml_filename='testing.zcml',
    gs_profile_id='groupdocs.assembly:testing',
    name="GROUPDOCS_ASSEMBLY")

GROUPDOCS_ASSEMBLY_INTEGRATION = IntegrationTesting(
    bases=(GROUPDOCS_ASSEMBLY, ),
    name="GROUPDOCS_ASSEMBLY_INTEGRATION")

GROUPDOCS_ASSEMBLY_FUNCTIONAL = FunctionalTesting(
    bases=(GROUPDOCS_ASSEMBLY, ),
    name="GROUPDOCS_ASSEMBLY_FUNCTIONAL")
