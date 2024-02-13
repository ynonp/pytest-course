import numpy as np
import random
display = ['.', 'X', 'O']

class TicTacToeGame:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        if random.randint(0, 100) > 50:
            self.player = 1
        else:
            self.player = 2

    def play(self, row: int, column: int):
        if self.board[row, column] != 0:
            return

        self.board[row, column] = self.player
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def parse_user_input(self, user_input) -> tuple[int, int]:
        pass

    def __str__(self):
        to_print = np.where(
            self.board == 1, 'X',
            np.where(self.board == 2, 'O', '.'))
        return '\n'.join([' '.join(to_print[i]) for i in range(3)])

    def print_board_2(self):
        for i in range(3):
            for j in range(3):
                print(display[self.board[i, j]], end='')
            print('')

    def print_board(self):
        print(self)

    def has_winner(self):
        pass

    def game_over(self):
        return len(self.board[self.board != 0]) == 9


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play(0, 0)
    game.print_board()
    # while not game.game_over():
    #     game.print_board()
    #     next_move = input()
    #     row, columns = game.parse_user_input(next_move)
    #     game.play(row, columns)
    #     if game.has_winner():
    #         print(f"Bravo!")
