# import3dCoat

Imports objs from 3DCoat that have been exported from 3DCoat. 
(uncheck "export constructor" or displacement depth value doesn't get exported).

Redshift or Octane materials will be created and assigned automatically.
Modify the importObj settings to not import materials!

**! We are not 100% sure we found the right settings yet, so please provide feedback !**

## Usage:
* Export .obj from 3dCoat (uncheck "export constructor") into a separate folder
* In Cinema4D make sure your obj import settings don't import material
* Set your Renderer to either Redshift or Octane
* Run the Importer (plugins->import3DCoat) and select the export folder
* wait for the import to finish...

## Notes:
* Diplacement nodes get created but are not plugged in by default
* the existence of specular_color decides if metalness or specular import options will be used

## Example Video:
[3DC_C4D_PBR on Vimeo](https://vimeo.com/280255790)
