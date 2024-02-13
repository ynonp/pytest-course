"""
Create 2 functions in the game:
save(file) - saves the board to a file
load(file) - restores game from file

Write tests to verify it works

Work time until: 12:40
"""
import os
from game.tic_tac_toe import TicTacToeGame


def test_save_load(game, game_temp_filename):
    game.play(0, 0)
    game.save(game_temp_filename)
    game2 = TicTacToeGame()
    game2.load(game_temp_filename)
    assert game2.__str__() == 'X . .\n. . .\n. . .'
