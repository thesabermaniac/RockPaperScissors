import random
cpu = random.randint(1, 3)
user = input('Choose your weapon (Rock, Paper, or Scissors): ')
while cpu == 1 and user.lower() == 'rock' \
        or cpu == 2 and user.lower() == 'paper' \
        or cpu == 3 and user.lower() == 'scissors':
    print('You\'ve tied with the computer. Please try again.')
    user = input('Choose your weapon (Rock, Paper, or Scissors): ')


def main():
    user_wins()
    cpu_wins()


def user_wins():
    if user.lower() == 'rock' and cpu == 3:
        print('The computer chose Scissors.')
        print('User wins!')
    elif user.lower() == 'paper' and cpu == 1:
        print('The computer chose Rock.')
        print('User wins!')
    elif user.lower() == 'scissors' and cpu == 2:
        print('The computer chose Paper.')
        print('User wins!')


def cpu_wins():
    if user.lower() == 'rock' and cpu == 2:
        print('The computer chose Paper.')
        print('The computer wins :(')
    elif user.lower() == 'paper' and cpu == 3:
        print('The computer chose Scissors.')
        print('The computer wins :(')
    elif user.lower() == 'scissors' and cpu == 1:
        print('The computer chose Rock.')
        print('The computer wins :(')


main()
