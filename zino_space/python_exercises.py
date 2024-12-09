# Exercise 1.1
a = 3 + 1
print(a)

b = 3 * 3
print(b)

c = 2 ** 3
print(c)

d = "Hello, world!"
print(d)
# 1.2 see script.py

# 1.3
# a - combines them into one word "python"
# b - types "py" three times then combines it with "thon" to create "pypypython"
# c - Error. Cannot use the minus operator for two string operands
# d - Error. Cannot concatenate a string with an integer
# e - Prints 3 three times
# f - Error. Undefined name variable
# g - Initializes and assigns 3 to the variable "a"
# h - Prints out 3

# 1.4
# a - Prints out True because the statement is true
# b - Prints out True because 1 is the boolean logic for True
# c - Prints out False because 0 is not the boolean logic for True
# d - Prints out True because 0 is the boolean logic for False
# e - Prints out True because the statment is true
# f - Prints out 0 because 3 is not equivalent to 1 and therefore 0 is placed in the parentheses representing the boolean logic for False which then gets multiplied by 3 giving 0
# g - Prints out False because 1 comes out the parentheses then gets multiplied by 4 and added by 3 to make 7, and 7 is not equivalent to 1 so its false
# h - Prints out False because 3**5 is not greater than or equal to 4**4

# 1.5
# a - Prints out 1.667
# b - Prints out 2 because that is the remainder
# c - Prints out 1.667 because data type conversion favors float over integer
# d - Prints out 1.667 because data type conversion favors float over integer
# e - Prints out the remainder 2.2 due to data type conversion
# f - Prints a large number equivalent to 2001 raised to the power of 200

# 1.6
# a - Error. Value is to large causing an overflow in storage
# b - Prints 1.0
# c - Prints 0.0 because exponents aren't included

# 1.7
name = "Zino Areh"
print(f'Hello, {name}!')

# 1.8
# a - Converts value into a float and prints out 123.0
# b - Converts value into a float and prints out 123.0
# c - Prints out 123.23 since its already a float data type
# e - Converts value into an integer and prints out 123
# f - Converts value into a float then converts it into an integer and prints out 123
# g - Converts value into a string and prints out '12'
# h - Converts value into a string and prints out '12.2'
# i - Converts value into boolean logic and prints out True
# j - Converts value into boolean logic and prints out False
# k - Converts value into boolean logic and prints out True


# Exercise 2
# 2.1
# return range(0, 5) because it automatically sets the range from 0 to 5
# for i in range(5) sets a range from 0 to 5. It won't output into the console
# type(range(5)) gives you the class for range. The type function tells you what the class or data type is.

# 2.2
# a
for i in range(101):
    print(i)
# b
for j in range(101):
    if (j % 7 == 0):
        print(j)
# c
for k in range(1, 101):
    if (k % 5 == 0) and (k % 3 != 0):
        print(k)
# d
x = int(input("Enter a number: "))
for l in range(2, 21):
    if (x % l == 0) and (x != l):
        print(l)
# 2.3
# a
numbers = 0
while (numbers != 101):
    print(numbers)
    numbers += 1
val = 0
while val != 101:
    if val % 7 == 0:
        print(val)
        val += 1
