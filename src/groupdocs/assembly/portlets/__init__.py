from zope.i18nmessageid import MessageFactory
PloneMessageFactory = MessageFactory('plone')

from Products.CMFCore.permissions import setDefaultRoles
setDefaultRoles('assembly.portlets.gdassembly: Add GroupDocs Assembly portlet',
                ('Manager', 'Site Administrator', 'Owner',))
