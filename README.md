plone-groupdocs-assembly-source
=============================

GroupDocs Assembly plugin for Plone CMS (Source code)

=============================

###Plugin installation steps:

When plugin is available only on GitHub (not released to Pypi) it can be installed with buildout like this:

* Create groupdocs.assembly folder under 'C:\Plone42\src\' folder
* Download files from GitHub and copy all the files into created folder.
* Change buildout.cfg file:
* Add groupdocs.assembly record into 'eggs =' section
* Add src/groupdocs.assembly into 'develop =' section
* Run buildout '.\bin\buildout.exe' from Plone installation folder(For example 'C:\Plone42').
* Restart plone.
* Go to Admin->Site setup ( http://localhost:8080/PloneGD/@@overview-controlpanel )
* Open Add-ons section ( http://localhost:8080/PloneGD/prefs_install_products_form )
* Find GroupDocs Assembly 1.0 add-on, check it and activate it.

###Using plugin:
* Modify or create a new page
* Click 'Mange Portlets'
* Open 'Add portlet..' dropbox and choose GroupDocs Assembly portlet
* Configure portlet's parameters and press Save button
* Open the created page ( http://localhost:8080/PloneGD/gd-test )  - GD Assembly Plug-in will be embeded into portlet region


###Sign, Manage, Annotate, Assemble, Compare and Convert Documents with GroupDocs
* [GroupDocs Assembly - HTML5 PDF Viewer tool for Plone CMS]( http://groupdocs.com/apps/assembly )

###Created by [GroupDocs Marketplace Team]( http://groupdocs.com/marketplace/ ).
