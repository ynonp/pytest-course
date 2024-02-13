class TicTacToeGame:
    def play(self, row: int, column: int):
        pass

    def parse_user_input(self, user_input) -> tuple[int, int]:
        pass

    def print_board(self):
        pass

    def has_winner(self):
        pass

    def game_over(self):
        pass


game = TicTacToeGame()
while not game.game_over():
    game.print_board()
    next_move = input()
    row, columns = game.parse_user_input(next_move)
    game.play(row, columns)
    if game.has_winner():
        print(f"Bravo!")
