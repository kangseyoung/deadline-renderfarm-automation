import sys
import os
import sys
sys.path.append("C:/Users/user/AppData/Local/Programs/Python/Python310/Lib/site-packages")
try:
    from PySide6.QtWidgets import QWidget, QApplication
    from PySide6.QtCore import Qt

    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile
    from PySide6.QtGui import QPixmap
    USING_QT = "PySide6"
except ImportError:
    from PySide2.QtWidgets import QWidget, QApplication,QMainWindow
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import QFile
    from PySide2.QtGui import QPixmap
    from PySide2.QtCore import Qt

    USING_QT = "PySide2"
import logging 
from gpclean.logging_setup import wtflogset
wtflogset()
main_window = None
class Submitter(QWidget):

    def closeEvent(self, event):
        global main_window
        main_window = None
        if self.ui:
            self.ui.deleteLater()
        self.deleteLater()
        event.accept()

    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        logging.info(f"Submitter에 전달된 model 타입: {type(model)}")
        try:
            logging.info("ReplaceA Submitter 생성자 진입")
            self.model = model  # ReplaceA 전달된 모델 저장
            self.setup_ui()
        except Exception as e:
            logging.info(f" Submitter 초기화 실패: {e}")


    def setup_ui(self):
        logging.info(" Submitter: setup_ui() 진입")

        # 절대경로로 변환 (패키지 구조에서도 안전하게 작동)
        ui_file_path = os.path.join(os.path.dirname(__file__), "main.ui")
        logging.info(f" UI 파일 경로: {ui_file_path}")

        if not os.path.exists(ui_file_path):
            logging.info(" UI 파일이 존재하지 않습니다.")
            return

        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            logging.info(" UI 파일을 열 수 없습니다.")
            return

        self.ui = loader.load(ui_file)
        ui_file.close()

        if self.ui is None:
            logging.info(" UI 로딩 실패")
            return

        self.ui.show()
        logging.info("ReplaceA UI 화면 show() 호출됨")
        self.veiw_info()
        logging.info("ReplaceA UI 로딩 완료")


    ###################################################################
    def set_current_path(self):
        logging.info(" set_current_path() 호출됨")
        text = self.model.get_current_path()
        self.ui.current_path.setText(text)

    def set_ouput_path(self):
        logging.info(" set_ouput_path() 호출됨")
        text = self.model.get_ouput_path()
        self.ui.output_path.setText(text)

    def set_pc_group(self):
        logging.info(" set_pc_group() 호출됨")
        text = "text" #얘는 ,,,잘 모르겠다 안쓰는걸 할당해줘야할지,, 예약할 때, 받아야할지.,,
        #아님 내가 임의로 정해서 줘도될지... 
        self.ui.pcgroup.setText(text)

    def set_DCC_png(self):
        logging.info(" set_DCC_png() 호출됨")
        png = "ui\\image\\menu1.png"
        pixmap = QPixmap(png)
        self.ui.DCC_png.setPixmap(pixmap)

    def set_profile_icon(self):
        logging.info(" set_profile_icon() 호출됨")
        png = "ui\\image\\usericon.jpg"
        pixmap = QPixmap(png)
        self.ui.usericon.setPixmap(pixmap)

    def set_studentID(self):
        logging.info(" set_studentID() 호출됨")
        text = self.model.get_studentID()
        self.ui.studentID.setText(text)

    def set_file_name(self):
        logging.info(" set_file_name() 호출됨")
        text = self.model.get_file_name()
        self.ui.filename.setText(text)

    def set_reservation_time(self):
        logging.info(" set_reservation_time() 호출됨")
        texts = self.model.get_reservation_list_for_student_id()
        self.ui.reservation_list.addItems(texts)

    def set_signed_time(self):
        text = self.model.get_signed_time()
        self.ui.signed_time.setText(text)

#####################################################################################
    def click_send_to_deadline(self):
        logging.info(" click_send_to_deadline() 연결 시작")
        self.ui.send_to_deadline.clicked.connect(self.test)
        logging.info("ReplaceA send_to_deadline 버튼 연결 완료")

    def test(self):
        
        logging.info(" 버튼 클릭됨: sendtodeadline")

    #####################################################################
    def veiw_info(self):
        logging.info(" veiw_info() 시작")
        self.set_current_path()
        self.set_ouput_path()
        self.set_pc_group()
        self.set_DCC_png()
        self.set_profile_icon()
        self.set_studentID()
        self.set_file_name()
        self.click_send_to_deadline()
        self.set_reservation_time()
        self.set_signed_time()
        logging.info("ReplaceA veiw_info() 완료")

if __name__ == "__main__":
    logging.info(" Submitter main 진입")
    app = QApplication(sys.argv)
    window = Submitter()
    window.show()
    logging.info("ReplaceA Submitter window.show() 완료")
    sys.exit(app.exec_())