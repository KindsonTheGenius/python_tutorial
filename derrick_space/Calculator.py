# ***** BUILDING CALCULATOR *****
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("Select an operation to perform: 1 - 6")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")

operation = input()

if operation == "1": # PERFORM ADDITION
   num1 = input("Enter First Number")
   num2 = input("Enter Second Number")
   print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2": # PERFORM SUBSTRACTION
    num1 = input("Enter First Number")
    num2 = input("Enter Second Number")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3": # PERFORM MULTIPLICATION
    num1 = input("Enter First Number")
    num2 = input("Enter Second Number")
    print("The total is " + str(int(num1) * int(num2)))
elif operation == "4": # PERFORM DIVISION
    num1 = input("Enter First Number")
    num2 = input("Enter Second Number")
    print("The total is " + str(int(num1) / int(num2)))
elif operation == "5":  # PERFORM SQUARE ROOT
    num = input("Enter Number")
    print("The squareroot is " + sqrt(num) )
elif operation == "4":  # PERFORM RAISE TO POWER
    num = input("Enter Number")
    print("The result is " )
else:
    print("Invalid Entry")