#Exercise 2.1

# range (5) prints automatically as range from(0,5)
n = 5
for i in range(5):
    print (i)

#console prints output as class 'range' with no value
for i in range(5):
    type(range(5))

#Exercise 2.2

#console prints numbers 0-100
for i in range(100):
    print (i)

#console prints an arithmetic progression of the number 7
for i in range(100):
    if i % 7 == 0:
        print (i)

#console prints out multiples of only 5
for i in range(100):
    if i % 5 == 0 and i % 3 != 0:
        print(i)



