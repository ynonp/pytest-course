import pytest
from game.tic_tac_toe import TicTacToeGame
import os

@pytest.fixture
def game():
    game = TicTacToeGame()
    game.player = 1
    yield game


@pytest.fixture
def game_temp_filename():
    yield "game.out"
    os.unlink("game.out")
