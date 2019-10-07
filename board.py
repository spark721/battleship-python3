
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
        hidden = self.hidden()
        print('\n\tThe game board\n')
        for i in range(self.size):
            print('\t' + ' '.join(hidden[i]))
        
        return ''

    def hidden(self) -> List[List[str]]:
        '''
        hide ships location
        should only reveal a hit spot
        return hidden_grid
        '''
        hidden_grid = self.grid
        
        for row in range(self.size):
            for col in range(self.size):
                pos = self.grid[row][col]
                if pos != 'X':
                    hidden_grid[row][col] = '~'
        
        return hidden_grid
