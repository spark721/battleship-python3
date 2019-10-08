
import os
import random
from typing import List

from ship import Ship

class Board():

    def __init__(self, size: int = 4):
        '''
        init grid and size default to 4 by 4
        run a loop to fill the grid
        '''
        self.size = size
        self.grid = list()
        self.num_ships = 0

        for row in range(self.size):
            row = list('~' * self.size)
            self.grid.append(row)


    def __str__(self) -> str:
        '''
        a dunder method to print the grid
        this will get invoked if print() was used on Board
        '''
        os.system('clear||cls')
        hidden_grid = self.hidden()
        print('\n\t* The game board *\n')
        print('\t   ', end='')
        
        for i in range(self.size):
            extra_space = ' ' if i < 10 else ''
            print(f'{i} {extra_space}',end='')
            if i + 1 == self.size: print('')
        for i in range(self.size):
            extra_space = ' ' if i < 10 else ''
            print(f'\t{i} {extra_space}' + '  '.join(hidden_grid[i]))
        
        return ''


    def cheat(self):
        os.system('clear||cls')
        print('\n\t* C H E A T   M O D E *\n')
        for i in range(self.size):
            print('\t' + ' '.join(self.grid[i]))
        
        print(f'\t* C H E A T   M O D E *')


    def hidden(self) -> List[List[str]]:
        '''
        hide ships location
        should only reveal a hit spot
        return hidden_grid
        '''
        return list(map(
            lambda row: list(map(
                lambda spot: 'X' if spot == 'X' else '~', 
                row)), 
            self.grid))


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


    def place_ship(self):
        '''
        create an instance of ship
        ship size is random between 2 and half of board size
        randomly position ship
        '''
        ship = Ship(random.randint(2, int(self.size / 2) + 1))
        ship.random_position(self)

        while True:
            if ship.valid_position(self): break
            else: ship.random_position(self)

        row = ship.pos[0]
        col = ship.pos[1]
        count = ship.size
        self.num_ships += ship.size

        while count > 0:
            self.grid[row][col] = 'S'
            if ship.vector == 'h':
                col += 1
            elif ship.vector == 'v':
                row += 1
            count -= 1
