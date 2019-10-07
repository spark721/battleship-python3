
import os
from typing import Dict, List

class Board():

    def __init__(self, size: int = 4):
        '''
        init grid and size default to 4 by 4
        run a loop to fill the grid
        '''
        self.size = size
        self.grid = list()

        for row in range(self.size):
            row = list('~' * self.size)
            self.grid.append(row)


    def __str__(self):
        '''
        a dunder method to print the grid
        this will get invoked if print() was used on Board
        '''
        os.system('clear||cls')
        hidden_grid = self.hidden()
        print('\n\tThe game board\n')
        for i in range(self.size):
            print('\t' + ' '.join(hidden_grid[i]))
        
        return ''


    def hidden(self) -> List[List[str]]:
        '''
        hide ships location
        should only reveal a hit spot
        return hidden_grid
        '''
        hidden_grid = list()
        
        for row in range(self.size):
            new_row = list('~' * self.size)

            for col in range(self.size):
                pos = self.grid[row][col]
                if pos == 'X': new_row[col] = 'X'

            hidden_grid.append(new_row)
        
        return hidden_grid


    def attack(self, row: int, col: int) -> bool:
        '''
        takes in a set of coordinate to attack
        check the given coordinate
        if ship ('S') is at the coordinate,
        update the grid to 'X' to indicate the hit
        return boolean
        '''
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            return True
        else:
            return False
