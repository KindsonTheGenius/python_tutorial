#number guessing game

import random

def number_guessing_game():
    print('\n\n')
    print('************************************')
    print('Welcome to the number guessing game!')
    print('*************************************')

    print('i have selected a number between 1 and 100. '
          'Can you guess it?')

    print("Type 'exit' to quit the game anytime. \n")

    my_number = random.randint(0, 100)
    attempts = 0

    user_input = input('Please enter your guess: >>   ')
    user_input = int(user_input)

    if(user_input == my_number):
        print("You win!")





number_guessing_game()

n = random.randint(1, 100)
print(n)
