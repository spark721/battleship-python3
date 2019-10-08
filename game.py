
from board import Board
from player import Player

class Game():

    def __init__(self):
        self.board = Board()
        self.player = Player()

    def start(self):
        pass

    def game_over(self, board, player) -> bool:
        return self.win(self.board, self.player) or self.lose(self.board, self.player)

    def win(self, board, player) -> bool:
        return self.board.num_ships == 0 and self.player.guess >= 0

    def lose(self, board, player) -> bool:
        return self.board.num_ships > 0 and self.player.guess == 0
