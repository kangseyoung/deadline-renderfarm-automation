import sys
import logging
from pathlib import Path
site_packages = Path.home() / "C:" / "Users" / "user" / "Documents" / "maya" / "2023"
if site_packages not in sys.path:
    sys.path.append(site_packages)
    logging.info("C:\\Users\\User\\OneDrive\\문서\\maya\\2023\\scripts sys.path.append중...")
try:
    from gpclean.ui.menu import create_menu
    if __name__ == "__main__":
        import maya.utils
        maya.utils.executeDeferred(create_menu)

except Exception as e:
    print(e)  # 전체 트레이스백 기록