import logging
import traceback
from logging_setup import wtflogset
wtflogset()
import sys
from pathlib import Path
logging.info(" 블렌더런처 진입")
custom_site_packages = Path.home() / "AppData" / "Roaming" / "Blender Foundation" / "Blender" / "4.2" / "scripts" / "modules" / "site-packages"
sys.path.insert(0, str(custom_site_packages))

import os
from pathlib import Path

# PySide2 설치된 경로
# shiboken2.dll이나 Qt5*.dll이 들어있는 폴더들 등록
os.add_dll_directory(str(custom_site_packages))
os.add_dll_directory(str(custom_site_packages / "PySide2"))
os.add_dll_directory(str(custom_site_packages / "shiboken2"))
os.add_dll_directory(str(custom_site_packages / "PySide2" / "Qt" / "bin"))

try:
    # PySide6 먼저 시도 → 실패하면 PySide2
    try:
        from PySide6.QtWidgets import QApplication
        USING_QT = "PySide6"
        logging.info("6됨")
    except ImportError:
        from PySide2.QtWidgets import QApplication
        USING_QT = "PySide2"
        logging.info("2됨22222222222222")

    logging.info(f" Loaded {USING_QT}")

    import sys
    from ui.login.login_view import LoginView
    from ui.login.login_controller import Receiver
    from ui.main.model import SubmissionDataModel
    from ui.main.view import Submitter

    login_window = None

    def launch_login_ui():
        global login_window
        logging.info(" launch_login_ui 진입")

        app = QApplication.instance()
        created_app = False
        if not app:
            logging.info(" QApplication 인스턴스가 없음 → 생성 필요")
            app = QApplication(sys.argv)
            created_app = True

        logging.info(" LoginView 인스턴스 생성")
        login_window = LoginView()

        logging.info(" Receiver 연결")
        receiver = Receiver(login_window)
        login_window.login_dictionary.connect(receiver.return_info)

        main_model = SubmissionDataModel()
        logging.info(" Model 연결")
        login_window.login_dictionary.connect(main_model.get_dictionary)

        login_window.show()
        logging.info(" login_window.show() 호출")

        if created_app:
            logging.info("새 엡 실행")
            sys.exit(app.exec_())

    # 🚀 시작 지점
    launch_login_ui()

except Exception as e:
    logging.error("🔥 예외 발생: UI 실행 중 문제가 생겼습니다.")
    logging.error(traceback.format_exc())
