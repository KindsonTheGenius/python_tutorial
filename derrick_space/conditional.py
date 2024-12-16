# Conditional Statements

# String
# Integer
# Float

# How to change score from string to integer/number?

score = input('Please enter your score: ')
score = int(score) # Convert to integer/number

#if score > 50:
#    print('Above Average')
#elif score < 50:                                     #else if
#    print('Below Average')
#elif score == 50:                                    # Comparison (==)
#    print('Average')

# Compute student grade

if score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
elif score >= 40:
    print("Grade D")
elif score >= 30:
    print("Grade E")
else:
    print("fail")

#1. Fix the problem a score above 100 should print 'Invalid Score'
#2. Score below 0 should print 'Invalid Score, score should not be negative"