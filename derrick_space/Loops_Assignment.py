'''
(b) Print the numbers 0 to 100 that are divisible by 7
(c) Print the numbers 1 to 100 that are divisible by 5 but not by 3
(d) Print for each of the numbers x = 2; : : : 20, all numbers that divide x, excluding 1 and x. Hence,
for 18, it should print 2 3 6 9.
'''
# Triple Quotes can do multiple line comments

#    % modulus

for i in range(100):
    if i%7 == 0:
        print(i)

