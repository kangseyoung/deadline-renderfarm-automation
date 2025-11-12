# ShaderMain.py (Maya 2023 호환 수정)
import glob
import os
import maya.cmds as cmds

# 상대 임포트 제거: 같은 폴더에 두 파일이 함께 있어야 함
import ShaderSetup as shader_setup


class MainWindow(object):
    def __init__(self):
        self._map_dict = {
            'base': None, 'height': None, 'metallic': None, 'normal': None, 'roughness': None,
            'anisotropy_angle': None, 'anisotropy_level': None, 'emissive': None
        }
        self._plus_color_switch = False
        self.set_window()

    def set_window(self):
        window_id = "autoShaderSetting"

        if cmds.window(window_id, ex=True):
            cmds.deleteUI(window_id)

        window = cmds.window(window_id, t='Substance Painter to Vray for Maya')
        cmds.columnLayout(adj=True, p=window)

        self.create_object_viewer()

        self.root_path = None
        cmds.textField('rootDirPath')
        cmds.button(l='BROWSE', c=self.get_path)

        cmds.text(l='Base Texture')
        self.create_colorspace_menu('base')

        cmds.text(l='Height Texture')
        self.create_colorspace_menu('height')

        cmds.text(l='Rough Texture')
        self.create_colorspace_menu('roughness')

        cmds.text(l='Normal Texture')
        self.create_colorspace_menu('normal')

        cmds.text(l='Metallic Texture')
        self.create_colorspace_menu('metallic')

        cmds.text(l='AnisotropyAngle Texture')
        self.create_colorspace_menu('anisotropy_angle')

        cmds.text(l='AnisotropyLevel Texture')
        self.create_colorspace_menu('anisotropy_level')

        cmds.text(l='Emissive Texture')
        self.create_colorspace_menu('emissive')

        cmds.button(l='RUN', bgc=(0.3, 0.6, 0.1), c=self.create_shader_nodes)

        cmds.showWindow(window)

    def create_object_viewer(self, *args):
        object_mesh = cmds.ls(dag=True, s=True, typ='mesh')
        transforms = []
        for model in object_mesh:
            node = cmds.listRelatives(model, p=True)[0]
            if cmds.nodeType(model) != 'camera' and node not in transforms:
                transforms.append(node)
        cmds.textScrollList('objectViewer', a=transforms, ams=True)

    def create_colorspace_menu(self, color_type):
        colorspace = {
            'arri_logc': 'ARRI LogC', 'camera_rec709': 'camera Rec 709',
            'sony_slog2': 'Sony SLog2', 'log_film_scam': 'Log film scam (ADX)',
            'cineon': 'Log-to-Lin (cineon)', 'jzp': 'Log-to-Lin (jzp)',
            'raw': 'Raw', 'aces2065_1': 'ACES2065-1', 'aces_cg': 'ACEScg',
            'cie_xyz': 'scene-linear CIE XYZ', 'dci_p3': 'scene-linear DCI-P3',
            'rec2020': 'scene-linear Rec 2020', 'rec709_srgb': 'scene-linear Rec709/sRGB',
            'gamma1.8': 'gamma 1.8 Rec 709', 'gamma2.2': 'gamma 2.2 Rec 709',
            'gamma2.4': 'gamma 2.4 Rec 709 (video)', 'sRGB': 'sRGB'
        }
        default_set = {
            'base': 'sRGB', 'height': 'Raw', 'metallic': 'Raw', 'normal': 'Raw', 'roughness': 'Raw',
            'anisotropy_angle': 'Raw', 'anisotropy_level': 'Raw', 'emissive': 'sRGB'
        }
        menu = cmds.optionMenu(color_type, l='COLORSPACE', en=True)
        for key, label in colorspace.items():
            cmds.menuItem(key, l=label)
        cmds.optionMenu(color_type, e=True, v=default_set[color_type])
        return menu

    def get_path(self, *args):
        # 폴더 선택
        file_name = cmds.fileDialog2(fm=3)[0]
        cmds.textField('rootDirPath', e=True, tx=str(file_name))
        self.root_path = cmds.textField('rootDirPath', q=True, tx=True)

        # 폴더 내의 모든 텍스처 후보 수집 (확장자는 필요에 맞게 추가)
        exts = ('*.exr', '*.tx', '*.tif', '*.tiff', '*.png', '*.jpg', '*.jpeg')
        map_list = []
        for ext in exts:
            map_list.extend(glob.glob(os.path.join(self.root_path, ext)))

        # Substance 네이밍 규칙(대/소문자 페어) 매핑
        pairs = [
            ('Base', 'base'),
            ('Height', 'height'),
            ('Metallic', 'metallic'),
            ('Normal', 'normal'),
            ('Roughness', 'roughness'),
            ('AnisotropyAngle', 'anisotropy_angle'),
            ('AnisotropyLevel', 'anisotropy_level'),
            ('Emissive', 'emissive'),
        ]

        # 각 채널에 해당하는 파일 리스트를 저장 (리스트로, Python3 호환)
        for upper, lower in pairs:
            matched = [p for p in map_list
                       if ('_' + upper) in os.path.basename(p) or ('_' + lower) in os.path.basename(p)]
            self._map_dict[lower] = matched

    def create_shader_nodes(self, *args):
        objects = cmds.textScrollList('objectViewer', q=True, si=True)
        for model in objects:
            shader_setting = shader_setup.ShaderSetter(model, self._map_dict)
            shader_setting.find_shader()
            shader_setting.create_shaders()
            shader_setting.create_dismap()
        opened_ui = cmds.lsUI(wnd=True)
        if 'expressionEditorWin' in opened_ui:
            cmds.deleteUI('expressionEditorWin')
