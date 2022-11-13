import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

project_path = sys.path[2]
ui_dir_path = 'ui_source'
file_name = 'main_view'
form_class = uic.loadUiType(f'../{ui_dir_path}/{file_name}.ui')[0]


class GUI(QMainWindow):     # class(super_class) QMainWindow 상속도 가능
    def __init__(self):
        """초기화 해주는 메서드
        :param
        self

        """
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Conimal')
        self.resize(600, 600)
        self.add_widgets()

    def add_widgets(self):
        self.statusBar().showMessage('Text in statusbar')
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        new_action = QAction('New', self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('New File')
        '''
        self.Pbtn1.clicked.connect(self.btn1_func)
        self.Pbtn2.clicked.connect(self.btn2_func)
        type the signal in this section
    def btn1_func(self):
        print("Pbtn1 Clicked")

    def btn2_func(self):
        print("Pbtn2 Clicked")
        '''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    app.exec_()

