import random

def number_guessing_game():
    print('\n\n')
    print('*************************************')
    print('Welcome to the Number Guessing Game')
    print('*************************************')

    print('I have selected a number between 1 and 2.'
          ' Can you guess it?')

    print("Type 'exit' to quit the game anytime.")

    # Generating a random number between 1 and 2
    my_number = random.randint(1, 2)
    attempts = 0

    while True:
        user_input = input('Please enter your guess: >>    ')

        # Check for exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Validate user input
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        user_input = int(user_input)
        attempts += 1

        if user_input == my_number:
            print(f"You Win! The number was {my_number}. It took you {attempts} attempts.")
            break
        else:
            print('Try again!')

number_guessing_game()
