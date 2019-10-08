
from board import Board
from player import Player

class Game():

    def __init__(self):
        self.player = Player()
        board_size = self.player.input_board_size()

        self.board = Board(board_size)

    def start(self):
        pass

    def game_over(self) -> bool:
        return self.win() or self.lose()

    def win(self) -> bool:
        return self.board.num_ships == 0 and self.player.guess >= 0

    def lose(self) -> bool:
        return self.board.num_ships > 0 and self.player.guess == 0

    def prep_board(self):
        '''
        takes in a board instance
        prepare the board by placing ships until
        board.num_ships is around 75% of player.guess
        '''
        while self.board.num_ships < int(self.player.guess * 0.75):
            self.board.place_ship()

    def attack(self):
        '''
        grab player input for attack coordinate
        attack on the coordinate
        if ship was hit,
        decrement num_ships on the board
        else, decrement player guess
        '''
        pos = self.player.input_pos(self.board.size)
        x = pos[0]
        y = pos[-1]
        if self.board.attack(y, x):
            print(f'\n\tDirect HIT at {pos}!')
            self.board.num_ships -= 1
        else:
            print(f'\n\tTarget missed at {pos}')
            self.player.guess -= 1
