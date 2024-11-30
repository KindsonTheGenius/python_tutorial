# Assignment 1 -  Write a simple python program that displays a text

def say_hello():
    print("Hello World") # This is an output statement
    # Write two more output statements

    full_name = 'Kindson Munonye'  # variable assignment

    first_name = 'Kindson'
    last_name = "Munonye"

    print(f"My name is {full_name}") # String interpolation by using f before the string

    print("What is your name: ")

if __name__ == "__main__":
    say_hello()