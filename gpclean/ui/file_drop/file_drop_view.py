# filedrop_view.py
from __future__ import annotations
import os
import sys
from datetime import datetime

# --- Qt import (PySide6 우선, 없으면 PySide2) ---
try:
    from PySide6.QtWidgets import QWidget, QApplication, QLabel
    from PySide6.QtCore import QObject, QEvent, QFile, Qt
    from PySide6.QtUiTools import QUiLoader
    USING_QT = "PySide6"
except ImportError:
    from PySide2.QtWidgets import QWidget, QApplication, QLabel
    from PySide2.QtCore import QObject, QEvent, QFile, Qt
    from PySide2.QtUiTools import QUiLoader
    USING_QT = "PySide2"

print(f"[filedrop_view] Loaded {USING_QT}")

# --- (선택) 네 로깅/리시버가 환경에 있으면 사용, 없으면 무시 ---
try:
    import logging
    from gpclean.logging_setup import wtflogset
    wtflogset()
except Exception:
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

try:
    from gpclean.ui.login.login_controller import Receiver  # noqa: F401
except Exception:
    Receiver = None  # 환경에 없으면 그냥 넘어감


# --- Maya 현재 디렉토리 얻기 ---
def get_current_dir_from_maya_or_os() -> str:
    """
    - 마야에서 실행: 씬 저장 경로(폴더) 또는 프로젝트 루트(workspace)
    - 마야 아닌 곳: 현재 작업 디렉토리
    """
    try:
        import maya.cmds as cmds  # type: ignore
        scene = cmds.file(q=True, sn=True)
        if scene:
            return os.path.dirname(scene)
        return cmds.workspace(q=True, rd=True)
    except Exception:
        # Maya가 아니거나 예외 시 OS 기준
        return os.getcwd()


# --- 드롭 처리용 필터 ---
class FileDropFilter(QObject):
    def eventFilter(self, obj, event):
        et = event.type()
        if et == QEvent.DragEnter:
            md = event.mimeData()
            if md and md.hasUrls():
                event.acceptProposedAction()
                return True
        elif et == QEvent.Drop:
            # 필요 시: dropped = [u.toLocalFile() for u in event.mimeData().urls()]
            print("hello qt")
            event.acceptProposedAction()
            return True
        return super().eventFilter(obj, event)


class FileDropView(QWidget):
    """
    - `filedrop.ui`(QMainWindow) 를 로딩하여 self.window로 보유
    - 라벨 currentdir / uploaddir / area 를 찾아 세팅
    """
    def __init__(self, ui_filename: str = "filedrop.ui", parent=None):
        super().__init__(parent)
        logging.info("FileDropView: __init__()")
        self.window = None
        self.drop_filter = FileDropFilter()
        self._build_ui(ui_filename)

    def _build_ui(self, ui_filename: str):
        # ui 파일은 이 파이썬 파일과 같은 폴더에 있다고 가정
        ui_path = os.path.join(os.path.dirname(__file__), ui_filename)
        logging.info(f"UI 파일 경로: {ui_path}")

        ui_file = QFile(ui_path)
        if not ui_file.exists():
            logging.error("UI 파일이 존재하지 않습니다!")
            return

        if not ui_file.open(QFile.ReadOnly):
            logging.error("UI 파일을 열 수 없습니다!")
            return

        try:
            loader = QUiLoader()
            self.window = loader.load(ui_file, self)  # parent=self
        finally:
            ui_file.close()

        if self.window is None:
            logging.error("UI 로딩 실패")
            return

        # 위젯 참조
        self.label_currentdir: QLabel = self.window.findChild(QLabel, "currentdir")
        self.label_uploaddir: QLabel = self.window.findChild(QLabel, "uploaddir")
        self.label_area: QLabel = self.window.findChild(QLabel, "area")

        # 현재 디렉토리 표시
        curdir = get_current_dir_from_maya_or_os()
        if self.label_currentdir:
            self.label_currentdir.setText(curdir)
        if self.label_uploaddir:
            # 업로드 경로도 기본은 현재 디렉토리로 표시(원하면 바꿔도 됨)
            self.label_uploaddir.setText(curdir)

        # 드롭 영역 설정
        if self.label_area:
            self.label_area.setAcceptDrops(True)
            self.label_area.installEventFilter(self.drop_filter)
            # 시각적으로 드롭 영역임을 조금 강조(원하면 스타일 조정)
            self.label_area.setAlignment(Qt.AlignCenter)
            if not self.label_area.text():
                self.label_area.setText("Drop files here")

        logging.info("FileDropView: UI 준비 완료")

    # 외부에서 호출: 창 띄우기
    def show_window(self):
        if self.window:
            self.window.show()
            self.window.raise_()
        else:
            logging.error("window가 생성되지 않았습니다. UI 로딩을 확인하세요.")


# --- 스탠드얼론 실행용 (마야 밖에서도 테스트 가능) ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = FileDropView(ui_filename="filedrop.ui")
    view.show_window()
    sys.exit(app.exec_())
