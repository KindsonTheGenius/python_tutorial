#Lists in Python

months = ['January', 'February',
          'March', 'April',
          'May', 'June',
          'July', 'August',
          'September', 'October', 'November'
          'December']

scores = [5, 100, 50, 70, 20, 30, 40, 15]

# scores.sort(reverse=True)
sorted_scores = sorted(scores)

index = scores.index(20)
#print(index)

# List Comprehensions

squares = [(x * x) for x in range(100) if x % 2 == 0]

#Nested List
x =[[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
#The first index is a row
#The second index is a column


print(x[0][1])

#Set, Tuple, Dictionary
set1 = (1,2,3,3)
list1 = [1,2,3,3]

mylist = [10, 20, 30, 40, 50]

last_element = mylist.pop()
print(last_element)

#Negative index
#len()
#pop

answer = mylist[1:3]
print(answer)


colors = ['red', 'green', 'blue']
colors[1] = 'yellow'
print(colors)


mylist = [2, 3, 4, 5, 2, 3, 4, 2]

count = 0
for i in mylist:
    if i == 2:
       count += 1
print(count)


mylist = ['a', 'b', 'c', 'a', 'b', 'a']

count = 0
for i in mylist:
    if i == 'a':
       count += 1
print(count)