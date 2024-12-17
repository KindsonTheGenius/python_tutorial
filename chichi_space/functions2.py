#Write a function to calculate sum of two numbers
"""
This function calculates the sum of two numbers
"""
def compute_sum(a, b, c):
    answer = a + b + c
    print(f'The sum is {answer}')
    return answer


#call the function
compute_sum(45, 89,32)

# default
# keyword
# positional


answer = 45

# variable-length arguments
def sum_up(*numbers):
    global answer
    answer = sum(numbers)
    print(f'The sum is {answer}')
    return answer


sum_up(10,10,10, 20, 20)

print(answer)