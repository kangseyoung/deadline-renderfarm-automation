
import os
import maya.cmds as cmds
import maya.mel as mel
import maya.utils
import logging 
from gpclean.logging_setup import wtflogset
wtflogset()

def create_menu():
    import maya.cmds as cmds
    try:
        from gpclean.main import launch_login_ui
        if cmds.menu("PRFS", exists=True):
            cmds.deleteUI("PRFS", menu=True)
            logging.info("기존 메뉴 PRFS 삭제함")

        # 부모를 'MayaWindow'로 하면 정상적으로 생성됨 (Python 방식)
        cmds.setParent("MayaWindow")
        cmds.menu("PRFS", label="PRFS", tearOff=True)
        cmds.menuItem(label="Submit to Deadline", parent="PRFS", command=lambda *_: launch_login_ui())

        logging.info("PRFS 메뉴 생성 완료")

    except Exception as e:
        logging.exception("메뉴 생성 중 에러 발생: %s", e)

    except Exception as e:
        logging.exception(e)