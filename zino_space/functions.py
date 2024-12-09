# 3.1
# a
def hello_world():
    print("Hello, world!")


# b
def hello_name(name):
    print("Hello, ", name)


# c
# print statements output a statement onto the console. Return statements stores a value from a function that can be used later on in the code
# If you use a return statment instead of a print it will store that value in the function and not output it into the console

# 3.2
def polynomial(x):
    """
    Evaluate the polynomial 3x^2 - x + 2 for a given value of x.
    """
    return 3 * x ** 2 - x + 2

x = int(input("Enter a value for x: "))
print("The result of the polynomial is:", polynomial(x))


# 3.3
# a
def my_max(x, y):
    if x > y:
        return x
    else:
        return y

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The larger number is:", my_max(x, y))
# b
def my_max2(a,b):
    if a > b:
        return a
    return b
print("-------------------------------")
print("My_max with only if statement")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The larger number is:", my_max2(a, b))