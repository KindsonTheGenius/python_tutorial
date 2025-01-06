import random


def number_guessing_game():
    def choose_difficulty():
        while True:
            print("\nChoose a difficulty level:")
            print("1. EASY (1-50)")
            print("2. MEDIUM (1-100)")
            print("3. HARD (1-200)")
            print("Type 'exit' to quit the game anytime.")
            try:
                choice = input("Enter your choice: ").strip()
                if choice.lower() == "exit":
                    print("Exiting the game. Goodbye!")
                    exit()
                difficulty = int(choice)
                if difficulty == 1:
                    return random.randint(1, 50), 1, 50
                elif difficulty == 2:
                    return random.randint(1, 100), 1, 100
                elif difficulty == 3:
                    return random.randint(1, 200), 1, 200
                else:
                    print("Invalid option. Please choose a valid difficulty.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3 or 'exit'.")

    def play_game(number_to_guess, val1, val2):
        attempts = 0
        while True:
            user_input = input(f"\nEnter your guess ({val1}-{val2}): ").strip()

            if user_input.lower() == "exit":
                print(f"You quit the game. The number was {number_to_guess}.")
                return False

            try:
                guess = int(user_input)
                if not (val1 <= guess <= val2):
                    print(f"Please enter a number between {val1} and {val2}.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return True

    print("Welcome to the Number Guessing Game!")

    while True:
        # Choose difficulty
        number_to_guess, val1, val2 = choose_difficulty()

        # Play the game
        game_won = play_game(number_to_guess, val1, val2)

        if game_won:
            while True:
                retry = input("Do you want to play again? (yes/no): ").strip().lower()
                if retry == "yes":
                    break
                elif retry == "no":
                    print("Thank you for playing the Number Guessing Game. Goodbye!")
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            # If the user quits mid-game, stop the game
            break


number_guessing_game()
