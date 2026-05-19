import logging
import os
import sys

def wtflogset():
    log_dir = "D:/new_maya"  # 로그 파일 경로
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "gpclean.log")

    # 공통 포맷터
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # 파일 핸들러
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # 콘솔 핸들러 (선택)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    # 루트 로거 설정
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[file_handler, stream_handler],
        force=True  # 기존 핸들러 전부 제거
    )

    # maya 및 PySide2 모듈 propagate 설정
    for mod_name in ["maya", "PySide2"]:
        logger = logging.getLogger(mod_name)
        logger.setLevel(logging.DEBUG)
        logger.propagate = True

    # PySide2 Qt 메시지 핸들러 연결
    try:
        from PySide2.QtCore import qInstallMessageHandler, QtMsgType

        def qt_message_handler(mode, context, message):
            level = {
                QtMsgType.QtDebugMsg: logging.DEBUG,
                QtMsgType.QtInfoMsg: logging.INFO,
                QtMsgType.QtWarningMsg: logging.WARNING,
                QtMsgType.QtCriticalMsg: logging.ERROR,
                QtMsgType.QtFatalMsg: logging.CRITICAL,
            }.get(mode, logging.INFO)
            logging.getLogger("Qt").log(level, message)

        qInstallMessageHandler(qt_message_handler)

    except ImportError:
        logging.warning("PySide2 not available; skipping Qt message handler setup.")
