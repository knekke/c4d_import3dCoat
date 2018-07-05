
# Import 3dCoat
# 
# Imports objs from 3DCoat that have been exported with the Unreal4 export settings 
# (uncheck "export constructor" or displacement depth value doesn't get exported).
#
# Redshift or Octane materials will be created and assigned automatically.
# Modify the importObj settings to not import Material!


import c4d
import os

# RedshiftWrapper https://github.com/gr4ph0s/C4D_RedshiftWrapper_API
import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

REDSHIFT_ID = 1036219
OCTANE_ID = 1029525

ID_OCTANE_DIFFUSE_MATERIAL = 1029501
ID_CREATE_GLOSSYMAT_PLUGIN = 1033893
ID_OCTANE_IMAGE_TEXTURE = 1029508
ID_OCTANE_MIX_TEXTURE = 1029505
ID_OCTANE_FALLOFF = 1029503
ID_OCTANE_MULTIPLY = 1029516
ID_OCTANE_INVERT = 1029514
ID_OCTANE_DISPLACEMENT = 1031901
ID_OCTANE_TRANSFORM = 1030961
ID_OCTANE_PROJECTION = 1031460
ID_COLOR = 5832

def load_bitmap(path):
    path = os.path.join(os.path.dirname(__file__), path)
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp.InitWith(path)[0] != c4d.IMAGERESULT_OK:
        bmp = None
    return bmp


class import3dCoat(c4d.plugins.CommandData):
    PLUGIN_ID = 1041375
    PLUGIN_NAME = 'import3dCoat'
    PLUGIN_INFO = 0
    PLUGIN_ICON = load_bitmap('res/icons/import3dcoat.tiff')
    PLUGIN_HELP = ''

    def Register(self):
        return c4d.plugins.RegisterCommandPlugin(
            self.PLUGIN_ID, self.PLUGIN_NAME, self.PLUGIN_INFO, self.PLUGIN_ICON,
            self.PLUGIN_HELP, self)

    def Execute(self, doc):
        rd = doc.GetActiveRenderData()
        self.renderer = rd[c4d.RDATA_RENDERENGINE]
        if self.renderer not in [REDSHIFT_ID, OCTANE_ID]:
            print "ABORT: Only Redshift and Octane supported at this point"
            return True
        doc.StartUndo()
        self.doc = doc
        location = c4d.storage.LoadDialog(0,"Select 3DCoat export Folder", flags=c4d.FILESELECT_DIRECTORY, def_path=doc.GetDocumentPath())
        objfiles = {}
        for file in os.listdir(location):
            ext = file.split('.')[-1]            
            if ext == 'obj':
                name = file.split('.')[0]
                objfiles[name] = os.path.join(location, file)
        for objname in objfiles.keys():
            obj = objfiles[objname]
            c4d.documents.MergeDocument(doc, obj, c4d.SCENEFILTER_OBJECTS, None)
            objects, materials = self.readObj(obj) 
            self.assignMaterials(objects, materials, objname)
        doc.EndUndo()
        c4d.EventAdd()
        return True

    def assignMaterials(self, objects, materials, objname):
        for obj in objects.keys():
            op = self.doc.SearchObject(obj)
            matname = objects[obj]['matname']
            if self.renderer == REDSHIFT_ID:
                tag = op.MakeTag(1036222) #RedshiftObject
                self.doc.AddUndo(c4d.UNDOTYPE_NEW, tag)
                tag[c4d.REDSHIFT_OBJECT_GEOMETRY_OVERRIDE] = 1
                tag[c4d.REDSHIFT_OBJECT_GEOMETRY_DISPLACEMENTENABLED] = 1
                tag[c4d.REDSHIFT_OBJECT_GEOMETRY_SUBDIVISIONENABLED] = 1
                tag[c4d.REDSHIFT_OBJECT_GEOMETRY_SMOOTHSUBDIVISIONENABLED] = 0
                mat, displValue = self.importMaterialRS(matname, materials[matname], objname)
                if displValue > 1:
                    tag[c4d.REDSHIFT_OBJECT_GEOMETRY_MAXDISPLACEMENT] = displValue
                else:
                    tag[c4d.REDSHIFT_OBJECT_GEOMETRY_DISPLACEMENTENABLED] = 0
                    tag[c4d.REDSHIFT_OBJECT_GEOMETRY_OVERRIDE] = 0
            elif self.renderer == OCTANE_ID:
                mat, displValue = self.importMaterialOCT(matname, materials[matname], objname)
            else:
                print("How did that happen???")
                return True
            textag = c4d.TextureTag()
            textag.SetMaterial(mat)
            textag[c4d.TEXTURETAG_PROJECTION]=c4d.TEXTURETAG_PROJECTION_UVW
            op.InsertTag(textag)
            
    def layerSet(self, name):
        root = self.doc.GetLayerObjectRoot() #Gets the layer manager
        LayersList = root.GetChildren() #Get Layer list
        for layer in LayersList:
            if layer.GetName() == name:
                return layer
        layer = c4d.documents.LayerObject()
        layer.SetName(name)
        layerRoot = self.doc.GetLayerObjectRoot()
        layer.InsertUnderLast(layerRoot)
        self.doc.AddUndo(c4d.UNDOTYPE_NEW,layer)
        return layer

    def importMaterialOCT(self, matname, textures, objname):
        mat = c4d.BaseMaterial(ID_OCTANE_DIFFUSE_MATERIAL)
        mat.SetName(objname + '_' + matname)
        mat[c4d.ID_LAYER_LINK] = self.layerSet(objname)
        mat[c4d.OCT_MATERIAL_TYPE] = 2511
        mat[c4d.OCT_MATERIAL_INDEX] = 1
        self.doc.InsertMaterial(mat) 
        self.doc.AddUndo(c4d.UNDOTYPE_NEW,mat)
        TransN = c4d.BaseShader(ID_OCTANE_TRANSFORM)
        mat.InsertShader(TransN)
        ProjN = c4d.BaseShader(ID_OCTANE_PROJECTION)
        mat.InsertShader(ProjN)

        if 'BaseColor' in textures:
            col = c4d.BaseShader(ID_OCTANE_IMAGE_TEXTURE)
            mat.InsertShader(col)
            col[c4d.IMAGETEXTURE_FILE] = textures['BaseColor']
            col[c4d.IMAGETEXTURE_MODE] = 0
            col[c4d.IMAGETEXTURE_GAMMA] = 2.2
            col[c4d.IMAGETEX_BORDER_MODE] = 0
            col[c4d.IMAGETEXTURE_TRANSFORM_LINK] = TransN
            col[c4d.IMAGETEXTURE_PROJECTION_LINK] = ProjN

        if 'Metalness' in textures:
            mixCol = c4d.BaseShader(ID_OCTANE_MIX_TEXTURE)
            mat.InsertShader(mixCol)
            mat[c4d.OCT_MATERIAL_DIFFUSE_LINK] = mixCol
            mixSpec = c4d.BaseShader(ID_OCTANE_MIX_TEXTURE)
            mat.InsertShader(mixSpec)
            mat[c4d.OCT_MATERIAL_SPECULAR_LINK] =mixSpec
            metal = c4d.BaseShader(ID_OCTANE_IMAGE_TEXTURE)
            mat.InsertShader(metal)
            metal[c4d.IMAGETEXTURE_FILE] = textures['Metalness']
            metal[c4d.IMAGETEXTURE_MODE] = 1
            metal[c4d.IMAGETEXTURE_GAMMA] = 1
            metal[c4d.IMAGETEX_BORDER_MODE] = 0
            metal[c4d.IMAGETEXTURE_TRANSFORM_LINK] = TransN
            metal[c4d.IMAGETEXTURE_PROJECTION_LINK] = ProjN
            colBlk = c4d.BaseShader(ID_COLOR)
            mat.InsertShader(colBlk)
            colBlk[c4d.COLORSHADER_COLOR] = c4d.Vector(0,0,0)
            colGrey = c4d.BaseShader(ID_COLOR)
            mat.InsertShader(colGrey)
            colGrey[c4d.COLORSHADER_COLOR] = c4d.Vector(0,0,0)
            invert = c4d.BaseShader(ID_OCTANE_INVERT)
            mat.InsertShader(invert)
            mixCol[c4d.MIXTEX_AMOUNT_LNK] = metal
            mixCol[c4d.MIXTEX_TEXTURE1_LNK] = col
            mixCol[c4d.MIXTEX_TEXTURE2_LNK] = colBlk
            mixSpec[c4d.MIXTEX_AMOUNT_LNK] = invert
            mixSpec[c4d.MIXTEX_TEXTURE1_LNK] = col
            mixSpec[c4d.MIXTEX_TEXTURE2_LNK] = colGrey
            invert[c4d.INVERT_TEXTURE] = metal
        else:
            mat[c4d.OCT_MATERIAL_DIFFUSE_LINK] = col

        if 'Roughness' in textures:
            roughtex = c4d.BaseShader(ID_OCTANE_IMAGE_TEXTURE)
            mat.InsertShader(roughtex)
            mat[c4d.OCT_MATERIAL_ROUGHNESS_LINK] = roughtex
            roughtex[c4d.IMAGETEXTURE_FILE] = textures['Roughness']
            roughtex[c4d.IMAGETEXTURE_MODE] = 1
            roughtex[c4d.IMAGETEXTURE_GAMMA] = 1
            roughtex[c4d.IMAGETEX_BORDER_MODE] = 0
            roughtex[c4d.IMAGETEXTURE_TRANSFORM_LINK] = TransN
            roughtex[c4d.IMAGETEXTURE_PROJECTION_LINK] = ProjN

        if 'Normal' in textures:
            normtex = c4d.BaseShader(ID_OCTANE_IMAGE_TEXTURE)
            mat.InsertShader(normtex)
            mat[c4d.OCT_MATERIAL_NORMAL_LINK] = normtex
            normtex[c4d.IMAGETEXTURE_FILE] = textures['Normal']
            normtex[c4d.IMAGETEXTURE_MODE] = 0
            normtex[c4d.IMAGETEXTURE_POWER_FLOAT] = 0.5
            normtex[c4d.IMAGETEXTURE_GAMMA] = 1
            normtex[c4d.IMAGETEX_BORDER_MODE] = 0
            normtex[c4d.IMAGETEXTURE_TRANSFORM_LINK] = TransN
            normtex[c4d.IMAGETEXTURE_PROJECTION_LINK] = ProjN
        
        if 'Displacement' in textures:
            displBmp = c4d.bitmaps.BaseBitmap()
            displBmp.InitWith(textures['Displacement'])
            size = displBmp.GetBw()
            if size < 512:
                detail = 9
            elif size < 1500:
                detail = 10    
            elif size < 3000:
                detail = 11
            elif size < 5500:
                detail = 12
            else:
                detail = 13
            disptex = c4d.BaseShader(ID_OCTANE_IMAGE_TEXTURE)
            mat.InsertShader(disptex)
            DISP = c4d.BaseShader(ID_OCTANE_DISPLACEMENT)
            mat.InsertShader(DISP)
            DISP[c4d.DISPLACEMENT_INPUT] = disptex
            DISP[c4d.DISPLACEMENT_MID] = 0.5
            DISP[c4d.DISPLACEMENT_LEVELOFDETAIL] = detail
            disptex[c4d.IMAGETEXTURE_FILE] = textures['Displacement']
            disptex[c4d.IMAGETEXTURE_MODE] = 1
            disptex[c4d.IMAGETEXTURE_GAMMA] = 1
            disptex[c4d.IMAGETEX_BORDER_MODE] = 0
            disptex[c4d.IMAGETEXTURE_TRANSFORM_LINK] = TransN
            disptex[c4d.IMAGETEXTURE_PROJECTION_LINK] = ProjN
        if 'displ_value' in textures:
            displValue = float(textures['displ_value'])
            if displValue > 1:
                mat[c4d.OCT_MATERIAL_DISPLACEMENT_LINK] = DISP
            DISP[c4d.DISPLACEMENT_AMOUNT] = displValue/100.0
        else: 
            displValue = 0
        return mat, displValue

    def importMaterialRS(self, matname, textures, objname):
        rs = Redshift()
        mat = rs.CreateMaterial()
        rs.SetMat(mat)
        mat.SetName(objname + '_' + matname)
        mat[c4d.ID_LAYER_LINK] = self.layerSet(objname)
        self.doc.InsertMaterial(mat) 
        self.doc.AddUndo(c4d.UNDOTYPE_NEW,mat)
        listNode = rs.GetAllNodes()
        MatNode = None
        OutPutNode = None
        for node in listNode:
            if node.GetType() == "Output":
                OutPutNode = node
            elif node.GetType() == "Material":
                MatNode = node
        MatNode.ExposeParameter(c4d.REDSHIFT_SHADER_MATERIAL_DIFFUSE_COLOR, c4d.GV_PORT_INPUT)
        MatNode.ExposeParameter(c4d.REDSHIFT_SHADER_MATERIAL_REFL_ROUGHNESS, c4d.GV_PORT_INPUT)
        MatNode.ExposeParameter(c4d.REDSHIFT_SHADER_MATERIAL_REFL_METALNESS, c4d.GV_PORT_INPUT)
        MatNode.ExposeParameter(c4d.REDSHIFT_SHADER_MATERIAL_BUMP_INPUT, c4d.GV_PORT_INPUT)
        MatNode[c4d.REDSHIFT_SHADER_MATERIAL_REFL_FRESNEL_MODE] = 2
        OutPutNode.ExposeParameter(c4d.GV_REDSHIFT_OUTPUT_DISPLACEMENT, c4d.GV_PORT_INPUT)

        if 'BaseColor' in textures:
            texCol = textures['BaseColor'] #r"H:\01_Projects\Daniel_Projects\3DC-C4D_Workflow\Export_to_C4D\Can01_default_color.png"
            texNodeCol=rs.CreateShader("TextureSampler", x=-100, y=200)
            texNodeCol.SetName('Tex Diffuse')
            texNodeCol[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_TEX0, c4d.REDSHIFT_FILE_PATH]=texCol
            rs.CreateConnection(texNodeCol, MatNode, 0, 0)

        if 'Roughness' in textures:
            texGloss = textures['Roughness'] #r"H:\01_Projects\Daniel_Projects\3DC-C4D_Workflow\Export_to_C4D\Can01_default_rough.png"        
            TexNodeGloss=rs.CreateShader("TextureSampler", x=-300, y=300)
            TexNodeGloss.SetName('Tex Roughness')
            TexNodeGloss[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_TEX0, c4d.REDSHIFT_FILE_PATH]=texGloss
            TexNodeGloss[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_TEX0_GAMMAOVERRIDE] = 1
            rs.CreateConnection(TexNodeGloss, MatNode, 0, 1)

        if 'Metalness' in textures:
            texMetal = textures['Metalness'] #r"H:\01_Projects\Daniel_Projects\3DC-C4D_Workflow\Export_to_C4D\Can01_default_metalness.png"
            TexNodeMetal=rs.CreateShader("TextureSampler", x=-100, y=400)
            TexNodeMetal.SetName('Tex Metalness')
            TexNodeMetal[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_TEX0, c4d.REDSHIFT_FILE_PATH]=texMetal
            TexNodeMetal[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_TEX0_GAMMAOVERRIDE] = 1
            rs.CreateConnection(TexNodeMetal, MatNode, 0, 2)

        if 'Normal' in textures:
            texNorm = textures['Normal'] #r"H:\01_Projects\Daniel_Projects\3DC-C4D_Workflow\Export_to_C4D\Can01_default_nmap.png"
            TexNodeNorm=rs.CreateShader("NormalMap", x=-100, y=500)
            TexNodeNorm.SetName('NormalMap')
            TexNodeNorm[c4d.REDSHIFT_SHADER_NORMALMAP_TEX0, c4d.REDSHIFT_FILE_PATH]=texNorm
            rs.CreateConnection(TexNodeNorm, MatNode, 0, 3)

        if 'Displacement' in textures:
            texDispl = textures['Displacement'] #r"H:\01_Projects\Daniel_Projects\3DC-C4D_Workflow\Export_to_C4D\Can01_default_disp.tif"
            DisplNode=rs.CreateShader("Displacement", x=-50, y=600)
            DisplNode.SetName('Displacement')
            DisplNode.ExposeParameter(c4d.REDSHIFT_SHADER_DISPLACEMENT_TEXMAP, c4d.GV_PORT_INPUT)

            TexNodeDispl=rs.CreateShader("TextureSampler", x=-250, y=600)
            TexNodeDispl.SetName('Tex Displacement')
            TexNodeDispl[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_TEX0, c4d.REDSHIFT_FILE_PATH]=texDispl
            rs.CreateConnection(TexNodeDispl, DisplNode, 0, 0)

        if 'displ_value' in textures:
            displValue = float(textures['displ_value'])
            if displValue > 1:
                rs.CreateConnection(DisplNode, OutPutNode, 0, 1)
            DisplNode[c4d.REDSHIFT_SHADER_DISPLACEMENT_SCALE] = displValue/2
            DisplNode[c4d.REDSHIFT_SHADER_DISPLACEMENT_NEWRANGE_MIN] = -0.5
            DisplNode[c4d.REDSHIFT_SHADER_DISPLACEMENT_NEWRANGE_MAX] = 0.5
        else: 
            displValue = 0

        if 'EmissiveColor' in textures:
            texEmit = textures['EmissiveColor'] #r"H:\01_Projects\Daniel_Projects\3DC-C4D_Workflow\Export_to_C4D\Can01_default_color.png"
            texNodeEmit=rs.CreateShader("TextureSampler", x=-300, y=200)
            texNodeEmit.SetName('Tex Emission')
            texNodeEmit[c4d.REDSHIFT_SHADER_TEXTURESAMPLER_TEX0, c4d.REDSHIFT_FILE_PATH]=texEmit
        return mat, displValue
     
    def readObj(self, objfile):
        dirname = os.path.dirname(objfile)
        with open(objfile,'r') as f:
            objlines = f.read().splitlines()
        objs = {}
        objname = ''
        for line in objlines:
            if line:
                split_line = line.strip().split(' ', 1)
                if len(split_line) < 2:
                    continue

                prefix, value = split_line[0], split_line[1]
                if prefix == 'g':
                    objname = value
                    objs[objname] = {'name' : value}
                # For files without an 'o' statement
                elif prefix == 'usemtl':
                    objs[objname]['matname'] = value
        with open(objfile.replace('.obj', '.mtl'), 'r') as f:
            mtllines = f.read().splitlines()
        materials = {}
        matname = ''
        for line in mtllines:
            if line:
                split_line = line.strip().split(' ', 1)
                if len(split_line) < 2:
                    continue
                prefix, data = split_line[0], split_line[1]
                if 'newmtl' in prefix:
                    matname = data
                    materials[matname] = {}
                elif prefix == 'map_Kd':
                    materials[matname]['BaseColor'] = dirname + '\\' + data
                elif prefix == 'map_Ks':
                    materials[matname]['Roughness'] = dirname + '\\' + data
                elif prefix == 'bump':
                    materials[matname]['Displacement'] = dirname + '\\' + split_line[-1].split('\\')[-1]
                    try:
                        materials[matname]['displ_value'] = split_line[-1].split(' ')[-2]
                    except:
                        materials[matname]['displ_value'] = 0
                elif prefix == 'map_bump':
                    materials[matname]['Normal'] = dirname + '\\' + data
        for matname in materials.keys():
            for i in os.listdir(dirname):
                for n in [matname, os.path.basename(objfile).split('.')[0]]:
                    if n+'_ao' in i.lower():
                        materials[matname]['ao'] = dirname + '\\' + i
                    if n+'_emissivecolor' in i.lower():
                        materials[matname]['EmissiveColor'] = dirname + '\\' + i
                    if n+'_metalness' in i.lower():
                        materials[matname]['Metalness'] = dirname + '\\' + i
                    if n+'_opacity' in i.lower():
                        materials[matname]['Opacity'] = dirname + '\\' + i
        return objs, materials

if __name__ == '__main__':
    import3dCoat().Register()
