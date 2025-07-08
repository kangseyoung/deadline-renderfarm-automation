bl_info = {
    "name": "GP Clean Blender Addon",
    "blender": (3, 0, 0),
    "version": (1, 0),
    "author": "Seyoung",
    "description": "Adds a menu item to launch GP Clean UI"
}

import bpy
import subprocess
import sys
from pathlib import Path
from gpclean.logging_setup import wtflogset
import logging 
wtflogset()

# Blender용 PySide2 수동 설치 위치 (네가 설치한 경로 맞춰서 수정해)
custom_site_packages = Path.home() / "AppData" / "Roaming" / "Blender Foundation" / "Blender" / "4.2" / "scripts" / "modules" / "site-packages"
sys.path.insert(0, str(custom_site_packages))
logging.info("gpclean __init__.py 로드됨")

def launch_tool():
    logging.info("launch_tool() 진입")
    launcher_path = Path(__file__).parent / "blender_launcher.py"
    logging.info(f"실행할 launcher_path: {launcher_path}")
    subprocess.Popen([sys.executable, str(launcher_path)])
    logging.info("subprocess.Popen 완료")

class GP_OT_LaunchGPUI(bpy.types.Operator):
    bl_idname = "gp.launch_login_ui"
    bl_label = "PRFS"

    def execute(self, context):
        logging.info("GP_OT_LaunchGPUI.execute() 호출됨")
        launch_tool()
        return {'FINISHED'}

def menu_func(self, context):
    logging.info("menu_func() 호출됨")
    self.layout.operator(GP_OT_LaunchGPUI.bl_idname)

def register():
    logging.info("register() 시작")
    bpy.utils.register_class(GP_OT_LaunchGPUI)
    bpy.types.TOPBAR_MT_editor_menus.append(menu_func)
    logging.info("register() 완료")

def unregister():
    logging.info("unregister() 시작")
    bpy.types.TOPBAR_MT_editor_menus.remove(menu_func)
    bpy.utils.unregister_class(GP_OT_LaunchGPUI)
    logging.info("unregister() 완료")
