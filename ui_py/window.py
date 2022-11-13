import sys

from componant import Conimal
from componant.time_manager import time_manager as tm
# from ui_py.main_view import Ui_main_window as ui
from ui_py.main_view import Ui_main_window as ui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import qdarkstyle as qd

import pyautogui as pg

import time

class window(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.conimal = Conimal.Conimal(age=1, name='검은고양이', friend_name='태결', update_status=self.update_bar)
        self._status_timer = tm(self.conimal.status_change_by_time)
        
        self.btn_cheer_up.clicked.connect(self.action_cheer)
        self.btn_play.clicked.connect(self.action_play)
        self.btn_start.clicked.connect(self.action_start)
        self.btn_feeding.clicked.connect(self.action_feed)
        self.btn_stop.clicked.connect(self.action_end)

    @pyqtSlot()
    def action_start(self):
        self.conimal_view.setPixmap(QPixmap(":./cat.png"))
        self.tbx_action.setText("시작!!")
        self._status_timer.cls.timer.start()
        
    @pyqtSlot()
    def action_play(self):
        self.conimal_view.setPixmap(QPixmap(":./cat_play.jpg"))
        self.tbx_action.setText(self.conimal._aff.love())

    @pyqtSlot()
    def action_feed(self):
        self.conimal_view.setPixmap(QPixmap(":./cat_eating.jpg"))
        self.tbx_action.setText(self.conimal._app.feed())

    @pyqtSlot()
    def action_cheer(self):
        self.conimal_view.setPixmap(QPixmap(":./cat_cheer.jpg"))
        self.tbx_action.setText(self.conimal._hea.cheer_up())
        time.sleep(1)
        pg.typewrite('메롱', interval=0.1)

    @pyqtSlot()
    def action_end(self):
        self.__del__()
        self.conimal.__del__()
        self._status_timer.cls.timer.__del__()
    
    def update_bar(self):
        self.pbr_appetite.setProperty("value", self.conimal._app.get_status())
        self.pbr_affection.setProperty("value", self.conimal._aff.get_status())
        self.pbr_health.setProperty("value", self.conimal._hea.get_status())

    def __del__(self):
        print('main window 닫힘!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qd.load_stylesheet_pyqt5())
    Window = window()
    Window.show()
    sys.exit(app.exec_())
