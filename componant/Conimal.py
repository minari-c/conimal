import sys

from PyQt5.QtGui import (
    QPixmap as q_pixmap
)

from PyQt5.QtCore import (
    QThread as q_thread,
    pyqtSlot as q_slot
)

from PyQt5.QtWidgets import (
    QApplication as q_app,
    QMainWindow as q_main,
)

from componant.status import (
    appetite,
    affection,
    health
)

from componant.time_manager import time_manager


class Conimal(object):
    """conimal class입니다.
    하나의 insatance만 존재하는 Singleton pattern으로 구현 되었습니다.

    프로필 [ 이름, 나이, 아이콘, 친구의 이름 ]
    상태 [ 굶주림, 애정도, 건강수치 ]
    행동 [ 애정표현, 먹기, 무작위 행동, ... ]

    Field:
        profile:
            name (str) : 코니멀의 이름

            age (int) : 코니멀의 나이

            icon (QtGui.QPixmap) : 코니멀의 image icon

            friend_name (str) : 사용자의 이름

        status:
            appetite (int) : 굶주림 정도

            affection (int) : 애정도

            health (int) : 건강 수치

    Methods:
         change_status(extern_signal) -> status에 영향

         dicide_action() -> 결정한 행동

         do_action(action) -> 행동
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Conimal, cls).__new__(cls)
            print("코니멀이 만들어졌습니다. (in __new__)")
        else:
            print("코니멀은 이미 존재합니다.")
        return cls._instance

    def __init__(
            self,
            name: str = '기본코니멀이름',
            age: int = -1,
            icon: q_pixmap = None,
            friend_name: str = '기본사용자이름',
            update_status: callable = None
    ) -> 'instance':
        cls = type(self)
        if not hasattr(cls, "_init"):
            cls._init = True

            self._name = name
            self._age = age
            self._icon = icon
            self._friend_name = friend_name

            self._app = appetite()
            self._aff = affection()
            self._hea = health()
            
            self.update_status = update_status
            
        self.view_info()

    def __del__(self):
        print(f'{self._name}가 사라집니다!')

    def view_info(self) -> '정보출력':
        print('\n')
        print("생성된 코니멀의 정보입니다.")
        print(f'코니멀의 이름은: {self._name}입니다.')
        print(f'코니멀의 나이는: {self._age}살입니다.')
        # print(f'코니멀의 사진은') alrt로 표시?
        print(f'코니멀은 {self._friend_name}의 친구에요!')

        print(f'코니멀은 현재 {self._app.get_status()}만큼 배고파요!')
        print(f'코니멀은 현재 {self._aff.get_status()}만큼 {self._friend_name}을 사랑해요!')
        print(f'코니멀은 현재 {self._hea.get_status()}만큼 건강해요!')

        # for k, v in self.__dict__.items():
        #     print(f'{k}: {v}')
        print()

    # @q_slot()   # pyqtSlot decorator
    def status_change_by_time(self) -> '시간에 따른 status 변화':
        self._app.change_by_time()
        self._aff.change_by_time()
        self._hea.change_by_time()
        
        self.update_status()
        
        print()
