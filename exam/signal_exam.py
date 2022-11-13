"""
form_signal.emit()            # signal과 연결된 slot을 동작
form_signal = signal()        # signal을 생성하기 위한 동작

signal을 임의로 정의하려면 QtCore.QObject를 상속 받아야한다.
class 초기화 시에 QtCore.QObject도 초기화 해야 한다.
반드시 signal은 class variable로 선언되어야 한다.
기본적으로 아래의 생성자를 가진다.
def __init__(self, parent):

my_signal = pyqtSignal([int], [str])

signal 연결 방법:
    1. QtCore.QObject.connect(widget, QtCore.SIGNAL(‘signalname’), slot_function) [외부에서]
    2. self.signal.connect(slot) 으로 연결해줄 수 있다. [내부에서]
"""
import sys


from PyQt5.QtGui import (
    QCloseEvent as q_close_event,
    QMouseEvent as q_mouse_event,
    QPointingDeviceUniqueId as point
)


# mouse button에 대한 static value가 들어있음
from PyQt5.QtCore import (
    QObject as q_object,
    # QCoreApplication as application,        # 
    pyqtSignal as q_signal,
    pyqtSlot as q_slot,
    QEvent as q_event,
    Qt as qt            # 마우스
)

from PyQt5.QtWidgets import (
    QApplication as q_app,
    QDialog as dialog
)


class mouse_signal(q_object):
    mouse_press = q_signal()

    def __init__(self):
        if not hasattr(self, 'mouse_press'):
            mouse_signal.my_signal = q_signal(mouse_signal)

    def mouse_click(self):
        self.mouse_press.emit()




class signal_exam(q_object):
    signal1 = q_signal()

    def run(self):
        self.signal1.



class window_view(dialog):
    def __init__(self):
        super().__init__()

        main_signal = signal_exam()
        main_signal.signal1.connect(self.signal1_slot)
        main_signal.run()

        mouse_click = mouse_signal().mouse_click
        mouse_click.connect(self.mousePressEvent)

    @q_slot()
    def signal1_slot(self):
        print('signal test')

    @q_slot()
    def mousePressEvent(self, a0: q_mouse_event) -> None:
        pass

    def closeEvent(self, a0: q_close_event) -> None:
        self.deleteLater()
        print(a0)


app = q_app(sys.argv)
window = window_view()
window.show()
app.exec_()


