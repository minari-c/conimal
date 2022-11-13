import sys

from PyQt5 import (
    QtWidgets as widget
)

from PyQt5.QtCore import (
    pyqtSlot as slot,           # 실제 동작을 위한 function
    pyqtSignal as signal        # Event
)


class Form(widget.QMainWindow):
    """main window class
    Methods:
    """

    # form_signal = signal()        # signal을 생성하기 위한 동작
    # form_signal.emit()            # signal과 연결된 slot을 동작
    """
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

    def __init__(self):
        super().__init__()

    @slot()



if __name__ == '__main__':
    app = widget.QApplication(sys.argv)
    window = Form()
    sys.exit(app.exec_())
