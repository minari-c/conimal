from PyQt5.QtCore import (
    QTimer as q_timer,
    QTime as q_time
)


class time_manager(object):
    """시간을 관리해주고 이벤트를 발생시킨다."""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(time_manager, cls).__new__(cls)

            print("time_manager가 만들어졌습니다. (in __new__)")
        return cls._instance

    def __init__(self, status_changer):
        self.cls = type(self)
        if not hasattr(self.cls, '_init'):
            self.cls.status_change_term = 1000
            self.cls.timer = q_timer()
            self.cls.timer.setInterval(self.cls.status_change_term)                   # timeout slot 반복 구간 정하기
            self.cls.timer.timeout.connect(status_changer)

    def __del__(self):
        print('timer가 멈춤니다!')
