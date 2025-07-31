import pytest

from game import Game
from game_result import GameResult


@pytest.fixture()
def game():
    return Game()


def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)


@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_input(game, invalid_input):
    assert_illegal_argument(game, invalid_input)


def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result._solved == solved
    assert result._strikes == strikes
    assert result._balls == balls


def test_return_solved_result_if_matched_number(game):
    game.question = "123"

    assert_matched_number(game.guess("123"), True, 3, 0)


def test_return_solved_result_if_unmatched_number(game):
    game.question = "123"
    result: GameResult = game.guess("456")

    assert_matched_number(result, False, 0, 0)


def test_return_solved_result_if_2strike(game):
    game.question = "123"
    result: GameResult = game.guess("124")

    assert_matched_number(result, False, 2, 0)
