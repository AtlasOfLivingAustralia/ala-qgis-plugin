Plugin Builder Results

Your plugin AlaQgisPlugin was created in:
    /Users/buy003/Documents/GitHub/alaQgisPlugin

Your QGIS plugin directory is located at:
    /Users/buy003/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins

What's Next:

  * requirements: 

  * Copy the entire directory containing your new plugin to the QGIS plugin
    directory

    pyuic5 -x alaQgisPlugin_dialog_base.ui  -o alaQgisPlugin_dialog_base.py  

  * Compile the resources file using pyrcc5 <== pyrcc5 -o resources.py resources.qrc 

  * Run the tests (``make test``)

  * Test the plugin by enabling it in the QGIS plugin manager

  * Customize it by editing the implementation file: ``alaQgisPlugin.py``

  * Create your own custom icon, replacing the default icon.png

  * Modify your user interface by opening AlaQgisPlugin_dialog_base.ui in Qt Designer

  * You can use the Makefile to compile your Ui and resource files when
    you make changes. This requires GNU make (gmake)

For more information, see the PyQGIS Developer Cookbook at:
http://www.qgis.org/pyqgis-cookbook/index.html

(C) 2011-2018 GeoApt LLC - geoapt.com
