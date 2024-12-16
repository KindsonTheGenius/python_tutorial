
while True: #while starts loop
    number = input('Please enter a number between 1 and 10:')
    number = int(number)
    if number > 10:
        print("Enter a number below 10")
    elif number < 10:
        print("Thank you")
        break #Ends the loop

for i in range(10):  #loop only runs 10 times
    print("Hello World")