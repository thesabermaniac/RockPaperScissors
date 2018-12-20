import random


def main():
    cpu = random.randint(1, 3)
    user = input('Choose your weapon (Rock, Paper, or Scissors): ')
    while tie_loop(user, cpu):
        cpu = random.randint(1, 3)
        user = input('Choose your weapon (Rock, Paper, or Scissors): ')
    user_wins(user, cpu)
    cpu_wins(user, cpu)
    print('Thanks for playing. Good bye.')


def user_wins(player1, player2):
    if player1.lower() == 'rock' and player2 == 3:
        print('The computer chose Scissors.')
        print('User wins!')
    elif player1.lower() == 'paper' and player2 == 1:
        print('The computer chose Rock.')
        print('User wins!')
    elif player1.lower() == 'scissors' and player2 == 2:
        print('The computer chose Paper.')
        print('User wins!')


def cpu_wins(player1, player2):
    if player1.lower() == 'rock' and player2 == 2:
        print('The computer chose Paper.')
        print('The computer wins :(')
    elif player1.lower() == 'paper' and player2 == 3:
        print('The computer chose Scissors.')
        print('The computer wins :(')
    elif player1.lower() == 'scissors' and player2 == 1:
        print('The computer chose Rock.')
        print('The computer wins :(')


def tie_loop(player1, player2):
    if player2 == 1 and player1.lower() == 'rock' \
            or player2 == 2 and player1.lower() == 'paper' \
            or player2 == 3 and player1.lower() == 'scissors':
        print('You\'ve tied with the computer. Please try again.')
        return True


main()
