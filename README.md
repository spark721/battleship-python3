
# Battleship

## Overview
A text-based battleship game for terminal or command prompt

## Technology used
- Object-orient programming
- python 3.7.4
- python modules
    - `os` (built-in)
    - `random` (built-in)
    - `time` (built-in)
    - `typing` (built-in)

## Instruction
- This game must be run with Python 3.6 or above

- Check your python version

        $ python --version

        $ python3 --version

- Execute main.py with python3 to start the game
        
        $ python3 main.py

- Game board
    - Default grid
    ```
       0  1  2  3
	0  ~  ~  ~  ~
	1  ~  ~  ~  ~
	2  ~  ~  ~  ~
	3  ~  ~  ~  ~
    ```

- Game play
    - Enter X and Y coordinate in that order to attack. Column first, then Row

## Feature
- Dynamic grid size. Default grid is set to 4 x 4, but the player may choose the grid size between 4 and 12

- My favorite part of this project was using lambda functions

    - For example, in the below sample code, I used `map function` with `lambda function` to convert string input form to integers

        ```python
        user_input = tuple(map(lambda n: int(n), user_input.split()))
        ```

    - Another example, a `nested` `map` and `lambda functions` and `ternary operator` to create the game board that does not reveal ships position. 

        ```python
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
        ```
