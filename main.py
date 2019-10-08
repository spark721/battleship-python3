
from game import Game

def play_again() -> bool:
    while True:
        play_again = input('\nPlay again? (Yes or No) ')
        if play_again.lower() == 'yes' or play_again.lower() == 'y':
            return True
        elif play_again.lower() == 'no' or play_again.lower() == 'n':
            return False

def main():
    '''
    initialize the game
    loop until player's answer is no
        start the game
            make board
            place ships
            make hidden board
            loop until game over
                render hidden with good hits
                player guess
                attack
        if game over, prompt user to play again
    terminate
    '''
    flag = True

    while flag:
        game = Game()
        game.start()
        flag = play_again()
    print('\nThank you for playing\n')

if __name__ == '__main__':
    main()
