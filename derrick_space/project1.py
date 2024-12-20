# Number Guessing Game

import random

def number_guessing_game():
    print('\n\n')
    print('*************************************')
    print('Welcome to the Number Guessing Game')
    print('*************************************')

    print('I have select a number between 1 and 100.' 
          ' Can you guess it?')

    print("Type 'exit' to quit the game anytime.")

    my_number = random.randint(0,5)
    attempts = 0

while True:
    user_input = input('Please enter your guess: >>    ')
    user_input = int(user_input)

    if user_input == 'exit':
        print(f"You quit the game. The number was {my_number}.")
        print('Goodbye')
        break

        user_input = int(user_input)
    if user_input == number_to_guess  :
        print(f'User input: {user_input}, My__number: {number_to_guess}')
        print("You win!")
        break

        #Increment Attempts
        attempts += 1

        #Check the guess
        if guess < number_to_guess:
            print("Too low! Try again loser.")
        elif guess > number_to_guess:
            print("Too high! Try again loser.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()

#n = random.randint(1,1000) <----- HOW YOU DO RANDOM NUMBER
#print(n)