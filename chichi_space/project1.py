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

    my_number = random.randint(0, 10)
    attempts = 0

    while True:
        user_input = input('Please enter your guess: >>   ')

        if user_input == 'exit':
            print(f"Thanks for playing. My number was {my_number}")
            print('Good bye!')
            break

        user_input = int(user_input)
        if user_input < 0 or user_input > 10:
            print('Please enter number between 0 and 10')
            continue

        attempts = attempts + 1

        if user_input < my_number:
            print('Number too low. Please increase it')
        elif user_input > my_number:
            print('Number too high. Please reduce it')
        else:
            print(f'Congratulations. You guessed the  number in {attempts} attempts')
            break

        if user_input == my_number:
            print(f'User input: {user_input}, My_number: {my_number}')
            print("You win!")
            exit() # we can also use break
        else:
            print('Try again')





number_guessing_game()

n = random.randint(1, 100)
print(n)
