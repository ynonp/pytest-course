from game.tic_tac_toe import TicTacToeGame
import pytest

def test_one_plus_one_is_two():
    assert (1 + 1) == 2

"""
First Task - 
1. Create a test (and implement the code)
to play the entire 3x3 board
and then:
assert game.game_over()

2. Implement game code

3. Verify our test passes
"""

def test_create_game():
    game = TicTacToeGame()
    assert not game.game_over()

def test_game_over_when_board_is_full():
    game = TicTacToeGame()
    for i in range(3):
        for j in range(3):
            game.play(i, j)
    assert game.game_over()

def test_play_in_the_same_place():
    game = TicTacToeGame()
    game.play(0, 0)
    game.play(0, 0)
    # TODO fix assertion and code for playing in the same place
    assert game.board[0, 0] == 1

def test_print_board():
    game = TicTacToeGame()
    game.play(0, 0)
    expected = """
X . .
. . .
. . .""".strip()
    assert(game.__str__() == expected)


def test_print_board():
    game = TicTacToeGame()
    game.play(0, 0)
    game.play(1, 1)
    game.play(2, 2)
    expected = """
X . .
. O .
. . X""".strip()
    assert(game.__str__() == expected)


def test_play_first_row():
    game = TicTacToeGame()
    game.play(0, 0) # X
    game.play(1, 1) # O
    game.play(0, 1) # X
    game.play(2, 2) # O
    game.play(0, 2) # X
    expected = """
X X X
. O .
. . O""".strip()
    assert (game.__str__() == expected)

def test_print_first_row():
    game = TicTacToeGame()
    game.board[0, :] = 1
    game.board[1, 1] = 2

    expected = """
X X X
. O .
. . .
    """.strip()
    assert (game.__str__() == expected)

def test_print_board_2(capsys):
    game = TicTacToeGame()
    game.play(0, 0)
    game.play(1, 1)
    game.play(2, 2)
    expected = """X..
.O.
..X
"""
    game.print_board_2()
    out, err = capsys.readouterr()
    assert out == expected



