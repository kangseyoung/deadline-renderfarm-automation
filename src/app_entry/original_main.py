import logging 
from gpclean.logging_setup import wtflogset
wtflogset()
# 루트 로거 설정
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
from gpclean.ui.login.login_view import LoginView
from gpclean.ui.login.login_controller import Receiver
from gpclean.ui.main.model import SubmissionDataModel
from gpclean.ui.main.view import Submitter
login_window = None  # 전역 변수로 유지

def launch_login_ui():
    global login_window
    logging.info(" launch_login_ui 진입")

    app = QApplication.instance()
    created_app = False
    if not app:
        logging.info(" QApplication 인스턴스가 없음 → 생성 필요")
        app = QApplication(sys.argv)
        created_app=True

    logging.info(" LoginView 인스턴스 생성3333333333333333")
    login_window = LoginView()

    logging.info(" Receiver 연결")
    receiver = Receiver(login_window)
    login_window.login_dictionary.connect(receiver.return_info)
    logging.info(" Receiver 딕셔너리 연결.")
    main_model = SubmissionDataModel()
    logging.info(" Model 연결")
    login_window.login_dictionary.connect(main_model.get_dictionary)
    logging.info(" Receiver 딕셔너리 연결.")
    login_window.show()
    logging.info(" login_window.show() 호출")

    # 마야 내에서는 필요 없음
    # sys.exit(app.exec())
    if created_app:
        logging.info("새 엡 실행")
        sys.exit(app.exec_())