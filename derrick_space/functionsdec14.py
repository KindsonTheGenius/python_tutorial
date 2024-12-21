# Write a function to calculate sum of two numbers

'''
This function calculate the sum of two numbers
'''
def compute_sum(a, b, c):
    answer = a + b + c
    print(f'The sum is {answer}')
    return answer

#Call the function
#compute_sum(45,12,65)

# 45, and 89 are arguments

answer = 45

#variable-length arguments
def sum_up(*numbers):
    global answer
    answer = answer +
    #print(f'The sum is {answer}')
    return answer

print(answer)
sum_up(10,10,10,20,20)