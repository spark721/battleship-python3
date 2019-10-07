
import random
from typing import List


class Ship():
    
    def __init__(self, size: int = 2, vector: str = 'h'):
        '''
        set default ship size to 2
        set vector to h for horizontal(default) or v for vertical
        set default position to 0, 0
        '''
        self.size = size
        self.vector = vector
        self.pos = [0, 0]


    def random_position(self, board):
        '''
        generate pseudo-random numbers
        for ship's starting position
        '''
        self.pos[0] = random.randrange(0, board.size)
        self.pos[1] = random.randrange(0, board.size)
        self.vector = random.choice(['h', 'v'])


    def valid_position(self, board) -> bool:
        '''
        check if a ship can be place on the grid
        '''
        row, col = self.pos[0], self.pos[1]

        if board.grid[row][col] == '~':
            if self.vector == 'v' and row + self.size < board.size:
                return True
            elif self.vector == 'h' and col + self.size < board.size:
                return True

        return False
