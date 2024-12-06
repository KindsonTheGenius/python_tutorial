# Exercise 1.3
a = 'py' + 'thon'
print(a)

b = "py" * 3 + "thon"
print(b)

# TypeError: unsupported operand type(s) for -: 'str' and 'str'
c = 'py' - 'py'
print(c)

# TypeError: can only concatenate str (not "int") to str
d = '3' + 3
print(d)

# console printed '333'
e = 3 * '3'
print(e)

# NameError: name 'a' is not defined
f = a
print(a)

# assigns 3  to the variable a
g = a = 3


# prints a as 3
h = a
print(h)

#Exercise 1.4

# prints out True
a = 1 == 1
print(a)

# prints out True because 1 represents the boolean logic for True
b = 1 == True
print(b)

# prints out False
c = 0 == True
print(c)

# prints out True  because 0 is the boolean logic for False
d = 0 == False
print(d)

# prints out True
e = 3 == 1 * 3
print(e)

# console prints result as 0
f = (3 == 1) * 3
print(f)

# console prints out variable as false
g = (3 == 3) * 4 + 3 == 1
print(g)

# console prints variable as false
h = 3**5 >= 4**4
print(h)

#Excercise 1.5

# prints out result value as 1.667
a = 5 / 3
print(a)

# prints result value as 2
b = 5 % 3
print(b)

# prints out result value as 1.667
c = 5.0 / 3
print(c)

# prints out result value as 1.667
d = 5 / 3.0
print(d)

# prints out result value as 2.2
e = 5.2 % 3
print(e)

# prints value as a large number representing 2001 ** 200
f = 2001 ** 200
print(f)

# Exercise 1.6

# OverflowError: (34, 'Result too large')
a = 2000.3 ** 200
print(a)

# prints value as 1.0
b = 1.0 + 1.0 - 1.0
print(b)

# prints value as 9e+20
c = 1.0 + 10e20 - 1.0e20
print(c)

# Exercise 1.8
#a - converts the float value and prints out 123.0
#b - converts the float value and prints out 123.0
#c - converts the float value and prints out 123.23
#d - converts the float value and prints out 123
#e - invalid literal for int() with base 10: '123.23'
#f - converts the float value and prints out 123
#g - converts the string value and prints out '12'
#h - converts the string value and prints out '12.2'
#i - converts the boolean value and prints out 'a' as True
#j - converts the boolean value and prints out '0' as False
#k - converts the boolean value and prints out 0.1 as True


