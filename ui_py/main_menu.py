import sys
from PyQt5.QtWidgets import (
    QMainWindow as Q_main,
    QApplication as Q_App
)

from PyQt5.QtGui import (
    QMouseEvent as QME
)
#    ui 파일을 불러오기 위한 패키지

#    form_class에 ui 파일을 로드한다.
# form_class = uic.loadUiType("../ui_source/main_view.ui")[0]


# main_win = Q_main()
# print(main_win())
# Main_view = Ui_MainWindow(main_win)

#    윈도우 클래스를 정의할 때 인자로 ui 파일인 form_class를 전달한다.

# print(Ui_MainWindow)
# print(QMainWindow)


class GUI(Q_main):
    """GUI class
    PyQt5에서 Event의 개념인 Signal을 Slot[func, method]과 연결해준다.

    super_class:
        QMainWindow
        form_class: .ui file [Qt Designer로 작성된 .ui를 읽어와서 상속받는다.]
    """
    def __init__(self):
        super().__init__()

    # self.setupUi(self)  # main_view의 메서드
        self.init_signal()

    def init_signal(self):
        self.Conimal.clicked.connect(self.mousePressEvent)
        print(self.Conimal.clicked)

    def change_status(self):
        self.Conimal.setText("complete")

    def mouseDoubleClickEvent(self, a0: QME) -> None:
        print(a0.buttons())
        print('마우스 더블 클릭')

    def mousePressEvent(self, a0: QME) -> None:
        print('마우스 클릭 완료')
        try:
            print(a0.buttons())
        except Exception as e:
            print(f'애러가 발생함 {e}')
        finally:
            self.closeEvent()

    def closeEvent(self) -> None:
        self.deleteLater()


if __name__ == "__main__":
    app = Q_App(sys.argv)
    gui = GUI()
    # gui.setWindowTitle('Conimal')
    gui.MainWindow.show()
    app.exec_()     # 이벤트 루프 생성

# https://m.blog.naver.com/sisosw/221419144691  PyQt
# http://www.hanul93.com/python-sphinx/ sphinx