from mimetypes import guess_type

from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성입니다.")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult | None:
        self.assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)
        return GameResult(False, 0, 0)


    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None입니다.")
        if len(guess_number) != 3:
            raise TypeError("입력은 3자리 문자열이어야 합니다.")
        if not guess_number.isdigit():
            raise TypeError("입력 문자열은 모두 숫자여야합니다.")
        if self._is_duplicated_number(guess_number):
            raise TypeError("입력 숫자 중 중복이 존재합니다.")

    def _is_duplicated_number(self, guessNumber):
        return len(set(guessNumber)) != 3
