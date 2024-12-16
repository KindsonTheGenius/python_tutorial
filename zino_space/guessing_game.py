import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Difficulty")
    print("1. EASY 1-50")
    print("2. MEDIUM 1-100")
    print("3. HARD 1-200")
    print("Type 'exit' to quit the game anytime.")
    print("\nChoose a difficulty level ")


    # Generate a random number
    while True:
        while True:
            try:
                difficulty = int(input())
                if difficulty == 1:
                    number_to_guess = random.randint(1,50)
                    val1 = 1
                    val2 = 50
                    break
                elif difficulty == 2:
                    number_to_guess = random.randint(1,100)
                    val1 = 1
                    val2 = 100
                    break
                elif difficulty == 3:
                    number_to_guess = random.randint(1,200)
                    val1 = 1
                    val2 = 200
                    break
            except ValueError:
                print("Invalid input. Please try again.")
                continue
        attempts = 0

        while True:
            # Get user input
            user_input = input("\nEnter your guess: ")

            # Allow user to quit
            if user_input.lower() == "exit":
                print(f"You quit the game. The number was {number_to_guess}.")
                break

            # Validate input
            try:
                guess = int(user_input)
                if guess < val1 or guess > val2:
                    print(f"Please enter a number between {val1} and {val2}.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            # Increment attempts
            attempts += 1

            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                try:
                    quit = input("Do you want to play again?(yes/no) ")
                    if quit == "yes":
                        print("Difficulty")
                        print("1. EASY 1-50")
                        print("2. MEDIUM 1-100")
                        print("3. HARD 1-200")
                        print("Type 'exit' to quit the game anytime.")
                        print("\nChoose a difficulty level ")

                        while True:
                            try:
                                difficulty = int(input())
                                if difficulty == 1:
                                    number_to_guess = random.randint(1, 50)
                                    val1 = 1
                                    val2 = 50
                                    break
                                elif difficulty == 2:
                                    number_to_guess = random.randint(1, 100)
                                    val1 = 1
                                    val2 = 100
                                    break
                                elif difficulty == 3:
                                    number_to_guess = random.randint(1, 200)
                                    val1 = 1
                                    val2 = 200
                                    break
                            except ValueError:
                                print("Invalid input. Please try again.")
                                continue
                        attempts = 0
                        continue
                    elif quit == "no":
                        print("Thank you for play the number guessing game. Goodbye!")
                        exit()
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue

number_guessing_game()