
class Player():
    
    def __init__(self):
        self.guess = 0

    def input_board_size(self) -> int:
        '''
        prompt user for board size
        '''
        while True:
            print('\nDefault grid size is 4')
            user_input = input('Select the grid size between 4 and 12: ')
            try:
                user_input = int(user_input)
            except:
                print(f'\tInvalid input: {user_input}')
            else:
                if user_input >= 4 and user_input <= 12:
                    return user_input
                else:
                    print(f'\tInvalid input: {user_input}')        

    def input_pos(self):
        pass
