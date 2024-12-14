import math

print("Select an operation to preform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE")
print("6. RAISE")

operation = int(input())

if operation == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The sum is "+str(num1 + num2))
elif operation == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The difference is " + str(num1 - num2))
elif operation == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The product is " + str(num1 * num2))
elif operation == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The result is " + str(num1 / num2))
elif operation == 5:
    num = int(input("Enter a number: "))
    print("The square root is %f " %(math.sqrt(num)))
elif operation == 6:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The result is %d " %(pow(num1, num2)))
else:
    print("Invalid Entry")