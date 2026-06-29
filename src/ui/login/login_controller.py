import logging
from gpclean.logging_setup import wtflogset
wtflogset()
logging.info(" Receiver 모듈 로드됨")

try:
    from PySide6.QtCore import QObject, Slot
    from PySide6.QtWidgets import QMessageBox
    USING_QT = "PySide6"
except ImportError:
    from PySide2.QtCore import QObject, Slot
    from PySide2.QtWidgets import QMessageBox
    USING_QT = "PySide2"
logging.info(f"ReplaceA Loaded {USING_QT}")

from gpclean.backend.authDB.db import auth_collection
import hashlib

from gpclean.ui.file_drop.file_drop_view import FileDropView

class Receiver(QObject):
    logging.info(" Receiver 클래스 정의됨")

    @Slot(object)
    def __init__(self,veiw):
        super().__init__()
        logging.info("ReplaceA Receiver: __init__() 실행됨")
        self.view = veiw

    #######################################################
    def return_info(self, dictionary):
        logging.info(" Receiver.return_info() 호출됨")
        self.dictionary = dictionary
        logging.info(" 로그인 입력 수신")
        self.db_dictionary = auth_collection
        self.get_info_if_exists()

    #######################################################
    def hash_password(self):
        password = self.dictionary["password"]
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return hashed

    def get_info_if_exists(self):
        logging.info(" get_info_if_exists(): DB에서 사용자 조회 중...")

        docs = auth_collection.find_one({"student_id": self.dictionary["student_id"]})
        logging.info(" 사용자 조회 완료")

        if docs:
            logging.info("ReplaceA 학번 존재함, 비밀번호 확인 중...")
            if docs["password_hash"] == self.hash_password():
                logging.info("ReplaceA 비밀번호 일치! 메인 UI로 이동!")
                self.open_main_win()
            else:
                logging.info(" 비밀번호 틀림")
                QMessageBox.warning(self.view.ui, "로그인 실패", "비밀번호가 틀렸습니다.")
        else:
            logging.info(" 학번 없음")
            QMessageBox.warning(self.view.ui, "로그인 실패", "학번이 틀렸습니다.")

    def open_main_win(self):
        from gpclean.ui.file_drop.file_drop_view import FileDropView

        a = FileDropView()
        a.show_window()


"""from gpclean.ui.main.model import SubmissionDataModel
        from gpclean.ui.main.view import Submitter
        # 모델 생성 및 값 설정
        model = SubmissionDataModel()
        model.get_dictionary(self.dictionary)
        # 글로벌에 저장하여 GC 방지
        import __main__
        __main__.main_ui = Submitter(model)
        __main__.main_ui.show()
        # 로그인 창 닫기
        self.view.ui.close()"""

        
"""    def open_main_win(self):
        logging.info(" open_main_win() 호출됨")
        try:
            from gpclean.ui.main.view import Submitter
            from gpclean.ui.main.model import SubmissionDataModel

            logging.info(" Submitter import 성공")

            # ReplaceA SubmissionDataModel을 먼저 만들고 dictionary 전달
            self.model = SubmissionDataModel()
            self.model.get_dictionary(self.dictionary)

            # ReplaceA Submitter에 model을 전달
            self.render_ui = Submitter(self.model)
            self.render_ui.show()

            logging.info("메인 UI 띄움")
        except Exception as e:
            logging.info(f" 메인 UI 열기 실패: {e}")"""
