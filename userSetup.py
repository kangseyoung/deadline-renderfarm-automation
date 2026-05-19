import sys
import logging
import os
from pathlib import Path

maya_script_path = os.getenv("MAYA_SCRIPT_PATH")
if maya_script_path:
    site_packages = Path(maya_script_path)
    if site_packages not in sys.path:
        sys.path.append(str(site_packages))
        logging.info("MAYA_SCRIPT_PATH added to sys.path")

try:
    from gpclean.ui.menu import create_menu
    if __name__ == "__main__":
        import maya.utils
        maya.utils.executeDeferred(create_menu)

except Exception as e:
    print(e)  # 전체 트레이스백 기록
