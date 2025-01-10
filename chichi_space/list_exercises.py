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

original = [1,2,3,4,5]

copy_list = original[0:5] # copy by slicing
copy_list.append(6)

copy_list2 = original + [6]


print(f"original list: {original}")
print(f"copied list: {copy_list}")
print(f"new copy: {copy_list2}")


#Bonus challenge
nested_list = [[1, 2],
               [3, 4],
               [5, 6]]

new_list = [item for row in nested_list for item in row]
print(new_list)

