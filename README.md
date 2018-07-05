# import3dCoat

Imports objs from 3DCoat that have been exported with the Unreal4 export settings 
(uncheck "export constructor" or displacement depth value doesn't get exported).

Redshift or Octane materials will be created and assigned automatically.
Modify the importObj settings to not import materials!

## Usage:
* Export .obj from 3dCoat (Unreal4 preset and uncheck "export constructor") into a separate folder
* In Cinema4D make sure your obj import settings don't import material
* Set your Renderer to either Redshift or Octane
* Run the Importer (plugins->import3DCoat) and select the export folder
* wait for the import to finish...
