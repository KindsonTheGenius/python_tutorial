#Functions
#Exercise 3.1
#a - console printed Hello world!
def hello_world():
    print("Hello world!")

hello_world()

#b
def hello_name(name):
    print(f"Hello, {name}!")

hello_name("Tina")

#c
#print is used to show the result or aby message while the program runs as an output
#return is used when you need the function to provide a result that can be stored or further processed
#if return is used instead of print, the function in question will give the value back to you which you can store it in a variable for later use; print would not.

#Exercise 3.2
#d
def polynomial(x):

    return 3 * x ** 2 - x + 2
x = int(input("Enter a value for x: "))
print("the result of the polynomial is:", polynomial(x))

#Exercise 3.3
#e
def my_max(x, y):
    if x > y:
        return x
    else:
        return y

#f
def my_max1(i, j):
    if i > j:
        return i
    return j
print("my_max with only if statement")





