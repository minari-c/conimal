class appetite:
    """굶주림을 나타내는 수치다."""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)

            print("appetite이 만들어졌습니다. (in __new__)")
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, '_init'):
            self._MAX_APPETITE_LEVEL = 5
            self._MAX_APPETITE_NUMERIC = 100
            self._MIN_APPETITE_NUMERIC = 0
            self._appetite_numeric = 0
            self._change_term = 3

    def get_status(self):
        return self._appetite_numeric

    def change_by_time(self):
        if self._appetite_numeric >= self._MAX_APPETITE_NUMERIC:
            print(f'appetite 수치가 너무 높아요! 밥주기 버튼을 눌러주세요!')
        else:
            self._appetite_numeric += self._change_term
            print(f'appetite 수치가 {self._appetite_numeric - self._change_term}에서 {self._appetite_numeric}로 바뀌었습니다! [증감폭: {self._change_term}]')

    def feed(self):
        temp = self._appetite_numeric - 30

        if temp < 0:
            return '[배부름!] 더이상 밥을 먹을 수 없어요!'
        else:
            self._appetite_numeric = temp
            return f'[밥줌!]appetite 수치가 {self._appetite_numeric - 30}에서 {self._appetite_numeric}로 바뀌었습니다! [증감폭: {30}]'


class affection:
    """애정을 나타내는 수치다."""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)

            print("affection이 만들어졌습니다. (in __new__)")
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, '_init'):
            self._MAX_AFFECTION_LEVEL = 5
            self._MAX_AFFECTION_NUMERIC = 100
            self._MIN_AFFECTION_NUMERIC = 0
            self._affection_numeric = 100
            self._change_term = -3

    def get_status(self):
        return self._affection_numeric

    def change_by_time(self):
        if self._affection_numeric <= self._MIN_AFFECTION_NUMERIC:
            print(f'affection 수치가 너무 낮아요! 놀이 버튼을 눌러주세요!')
        else:
            self._affection_numeric += self._change_term
            print(f'affection 수치가 {self._affection_numeric - self._change_term}에서 {self._affection_numeric}로 바뀌었습니다! [증감폭: {self._change_term}]')

    def love(self):
        temp = self._affection_numeric + 30

        if temp >= 100:
            return '[너무 좋아함!] 더 이상 좋아할 수 없어요!'
        else:
            self._affection_numeric += 30
            return f'[사랑!]affection 수치가 {self._affection_numeric - 30}에서 {self._affection_numeric}로 바뀌었습니다! [증감폭: {30}]'


class health:
    """건강을 나타내는 수치."""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)

            print("health가 만들어졌습니다. (in __new__)")
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, '_init'):
            self._MAX_HEALTH_LEVEL = 5
            self._MAX_HEALTH_NUMERIC = 100
            self._MIN_HEALTH_NUMERIC = 0
            self._health_numeric = 100
            self._change_term = -3

    def get_status(self):
        return self._health_numeric

    def __del__(self):
        print('health가 사라집니다!')

    def change_by_time(self):
        if self._health_numeric <= self._MIN_HEALTH_NUMERIC:
            print(f'health 수치가 너무 낮아요! 응원 버튼을 눌러주세요!')
        else:
            self._health_numeric += self._change_term
            print(f'health 수치가 {self._health_numeric - self._change_term}에서 {self._health_numeric}로 바뀌었습니다! [증감폭: {self._change_term}]')

    def cheer_up(self):
        temp = self._health_numeric + 30

        if temp >= 100:
            return '[너무 건강함!] 더 이상 건강해질 수 없어요!'
        else:
            self._health_numeric += 30
            return f'[응원!]health 수치가 {self._health_numeric - 30}에서 {self._health_numeric}로 바뀌었습니다! [증감폭: {30}]'

