
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
    - Enter X and Y coordinate in that order to attack. `Column` first, then `Row`
    - Players will lose their shots ONLY if they miss
    - A hit on enemy ship will NOT decrease your number of shots remaining

## Feature
- `Dynamic grid size`. Default grid is set to 4 x 4, but the player may choose the grid size between 4 and 12

- `Dynamic ship size` and `vector`. Ships will take up at minimum `2 spaces` and it may take up more depends on the size of the grid. Ship's vector is randomly selected between `horizontal` and `vertical`
    - That being said, if you successfully hit a enemy ship, there must be at least one more adjacent spot
- Code example for random ship size
    - Instantiating a Ship object from a Board class to place them on the grid
    ```python
    import random
    from ship import Ship
    class Board():
        # ... code omitted ...
        Ship(random.randint(2, int(self.size / 2) + 1))
    ```

- Code example for random ship vector
    ```python
    import random
    class Ship():
        # ... code omitted ...
        self.vector = random.choice(['h', 'v'])
    ```

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

- Another thing that I learned during this project is about the `print` function. The `print` function takes an `optional second argument` that is by default `'\n'` (a line break). This can be changed by passing in a second argument to a print function.

    - For example, I passed in an empty string as a second argument to print the x axis coordinates on top of the board
    ```python
    for i in range(self.size):
            extra_space = ' ' if i < 10 else ''
            print(f'{i} {extra_space}',end='')
            if i + 1 == self.size: print('')
    ```

## Cheat mode
- Implemented for debugging purposes during the development, but I have decided to make it available to players
- Instead of entering coordinates to attack, try typing in `CHEATER` (yes, all caps because you are cheating!)
- Surprise