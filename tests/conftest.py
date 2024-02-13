import pytest
from game.tic_tac_toe import TicTacToeGame

@pytest.fixture
def game():
    game = TicTacToeGame()
    game.player = 1
    yield game
