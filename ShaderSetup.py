# ShaderSetup.py (Maya 2023 호환 수정)
import re
import os
import maya.cmds as cmds
import maya.mel as mel


class ShaderSetter(object):
    def __init__(self, model, maps):
        self._model = model
        self._maps = maps
        self._vray_shader = None
        self._sg_node = None

    def check_sequential_texture(self, color_type, shader_name):
        # 리스트 컴프리헨션으로 확정 리스트 생성(Python3 호환)
        texture = [name for name in (self._maps.get(color_type) or []) if shader_name in name]
        tx_type = 'udim' if len(texture) > 1 else 'non_udim'
        return tx_type

    def create_texture_file_node(self, color_type):
        file_node = cmds.shadingNode('file', at=True, icm=True)
        file_node = cmds.ls(file_node, l=True)[0]
        color = cmds.optionMenu(color_type, q=True, v=True)
        cmds.setAttr('{}.ignoreColorSpaceFileRules'.format(file_node), True)
        cmds.setAttr('{}.colorSpace'.format(file_node), color, typ='string')

        # Python3: filter -> 리스트로 확정
        candidates = [x for x in (self._maps.get(color_type) or []) if self._vray_shader in x]
        if candidates:
            tx_type = self.check_sequential_texture(color_type, self._vray_shader)
            first = candidates[0]
            cmds.setAttr('{}.fileTextureName'.format(file_node), first, typ='string')
            if tx_type == 'udim':
                cmds.setAttr('{}.uvTilingMode'.format(file_node), 3)  # UDIM
        else:
            cmds.delete(file_node)
            return None

        tex_node = cmds.shadingNode('place2dTexture', au=True)
        tex_attrs = ('outUV', 'outUvFilterSize')
        file_attrs = ('uvCoord', 'uvFilterSize')
        for i in range(2):
            cmds.connectAttr('{}.{}'.format(tex_node, tex_attrs[i]), '{}.{}'.format(file_node, file_attrs[i]))
        common_attrs = (
            'vertexCameraOne', 'vertexUvOne', 'vertexUvThree', 'vertexUvTwo', 'coverage',
            'mirrorU', 'mirrorV', 'noiseUV', 'offset', 'repeatUV', 'rotateFrame', 'rotateUV',
            'stagger', 'translateFrame', 'wrapU', 'wrapV'
        )
        for attr in common_attrs:
            cmds.connectAttr('{}.{}'.format(tex_node, attr), '{}.{}'.format(file_node, attr))
        return file_node

    def find_shader(self):
        # 안전하게 SG/셰이더 찾기
        dag_node = cmds.ls(self._model, dag=True, s=True) or []
        sgs = cmds.listConnections(dag_node, t='shadingEngine') or []
        if not sgs:
            raise RuntimeError("No shadingEngine connected to {}".format(self._model))
        self._sg_node = sgs[0]

        shader = cmds.listConnections(self._sg_node) or []
        mats = cmds.ls(shader, materials=True) or []
        if not mats:
            raise RuntimeError("No material connected to {}".format(self._sg_node))
        self._vray_shader = mats[0]

        # VRay 속성 (존재하는 경우에만)
        if cmds.objExists(self._vray_shader + '.bumpMapType'):
            cmds.setAttr('{}.bumpMapType'.format(self._vray_shader), 1)
        if cmds.objExists(self._vray_shader + '.reflectionColor'):
            cmds.setAttr('{}.reflectionColor'.format(self._vray_shader), 1.0, 1.0, 1.0, typ='double3')

    def connect_attrs(self, nodes=None, aniso_rotation=None, aniso_level=None, emissive=None):
        # node index: [0]=dismap, [1]=base, [2]=height, [3]=metal, [4]=normal, [5]=rough
        cmds.connectAttr('{}.outColor'.format(nodes[1]), '{}.color'.format(self._vray_shader))
        cmds.connectAttr('{}.outAlpha'.format(nodes[2]), '{}.displacement'.format(nodes[0]))
        cmds.connectAttr('{}.outAlpha'.format(nodes[5]), '{}.reflectionGlossiness'.format(self._vray_shader))
        cmds.connectAttr('{}.outColor'.format(nodes[4]), '{}.bumpMap'.format(self._vray_shader))
        cmds.connectAttr('{}.outAlpha'.format(nodes[3]), '{}.metalness'.format(self._vray_shader))
        if emissive is not None:
            cmds.connectAttr('{}.outColor'.format(emissive), '{}.illumColor'.format(self._vray_shader))
        if aniso_level is not None:
            cmds.connectAttr('{}.outAlpha'.format(aniso_level), '{}.anisotropy'.format(self._vray_shader))
        if aniso_rotation is not None:
            cmds.connectAttr('{}.outAlpha'.format(aniso_rotation), '{}.anisotropyRotation'.format(self._vray_shader))

    def create_shaders(self):
        model = cmds.ls(self._model, fl=True)[0]
        flatten_data = cmds.polyListComponentConversion(model, tf=True)
        base_node = self.create_texture_file_node('base')
        height_node = self.create_texture_file_node('height')
        metal_node = self.create_texture_file_node('metallic')
        normal_node = self.create_texture_file_node('normal')
        rough_node = self.create_texture_file_node('roughness')
        anisotropy_angle_node = self.create_texture_file_node('anisotropy_angle')
        anisotropy_level_node = self.create_texture_file_node('anisotropy_level')
        emissive_node = self.create_texture_file_node('emissive')

        dismap_node = cmds.shadingNode('displacementShader', asShader=True)

        node_list = [dismap_node, base_node, height_node, metal_node, normal_node, rough_node]
        aniso_r_data = anisotropy_angle_node if anisotropy_angle_node else None
        aniso_l_data = anisotropy_level_node if anisotropy_level_node else None
        emiss_data = emissive_node if emissive_node else None
        self.connect_attrs(nodes=node_list, aniso_rotation=aniso_r_data, aniso_level=aniso_l_data, emissive=emiss_data)

        cmds.connectAttr('{}.displacement'.format(dismap_node), '{}.displacementShader'.format(self._sg_node))
        cmds.connectAttr('{}.outColor'.format(self._vray_shader), '{}.surfaceShader'.format(self._sg_node), f=True)

        if cmds.objExists(self._vray_shader + '.useRoughness'):
            cmds.setAttr('{}.useRoughness'.format(self._vray_shader), True)

        cmds.select(self._vray_shader, add=True)
        cmds.sets(flatten_data, e=True, fe=self._sg_node)
        cmds.select(self._vray_shader, d=True)

    def create_dismap(self):
        # VRay 디스플레이스먼트 노드 생성 (플러그인 로드 되어 있어야 함)
        dis_shader = cmds.createNode('VRayDisplacement', n=self._model+'_disp')
        cmds.select(self._model)
        cmds.select(dis_shader, add=True, ne=True)
        model = cmds.ls(sl=True)
        cmds.sets(model[0], e=True, fe=dis_shader)
        mel.eval('vrayDispSetting("{}");'.format(dis_shader))

        try:
            model_checker = cmds.listRelatives(dis_shader, c=True)
            if model_checker != []:
                return True
        except Exception:
            print('**  Failed to create Displacement shader!  **')
            return False
