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
                elif difficulty == 2
