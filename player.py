
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
                int(user_input)
            except:
                print(f'\tInvalid input: {user_input}')
            else:
                user_input = int(user_input)
                if user_input >= 4 and user_input <= 12:
                    self.guess = int(user_input * user_input / 2)
                    return user_input
                else: print(f'\tInvalid input: {user_input}')

    def input_pos(self, size: int) -> tuple:
        '''
        prompt user for attack position
        '''
        print('\n\tYour turn to attack')
        while True:
            print('\n\tEnter x and y coordinates separated by space')
            user_input = input(f'\t\t\t(between 0 and {size - 1}): ')
            try:
                if len(user_input.split()) != 2:
                    raise Exception
                int(user_input.split()[0])
                int(user_input.split()[-1])
            except:
                print(f'\t\tInvalid input: {user_input}')
                continue
            else:
                user_input = tuple(map(lambda n: int(n), user_input.split()))
                if user_input[0] < size and user_input[-1] < size:
                    return user_input
                else:
                    print(f'\t\tInvalid input: {user_input}')
