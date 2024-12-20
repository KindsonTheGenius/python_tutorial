# 7.1 Create a list named fruits
from os import remove

fruits = ["apple", "banana", "cherry"]

# Print the entire list
print(fruits)

# 7.2 Accessing List Elements
numbers = [10, 20, 30, 40, 50]

# a. Print the first element
print("First element:", numbers[0])

# b. Print the last element
print("Last element:", numbers[-1])

# c. Print the sublist containing the second and third elements
print("Sublist (second and third elements):", numbers[1:3])

# 7.3 Modify List elements
colors1 = ["red","green","blue"]
# Change green to yellow and print updated list
colors2 = ["red","yellow","blue"]
print(colors2)

# 7.4 Add elements to a list
# a. Create an empty list called animals
animals = []

# b. Append the following animals to the list one by one: cat, dog, bird
animals.append("cat")
animals.append("dog")
animals.append("bird")

# c . Print Final list
print(animals)

# 7.5 Remove elements from a list
pets = ["cat","dog","bird","fish"]

#a. remove bird using remove() method
pets.remove("bird")
#b. remove last element using the pop() method and print it.
#-------------------------------??????----------------------------------------------------
#c.Print updated list
print(pets)

# 7.6 List comprehension for EVen numbers
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Use list comprehension to create a list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Print list of even numbers
print(even_numbers)

# 7.7 Sort List in Ascending and Descending Order
Scores = [88,92,75,63,95,70]

# Sort list in ascending order and print
ascending_order = sorted(Scores)
print(ascending_order)
#Sort list in descending order and print
descending_order = sorted(Scores, reverse=True)
print(descending_order)

#7.8 Max & Min Values
Temperatures = [23,19,30,25,22,18,27]
#Max Temp print
maximum_temperature = max(Temperatures)
print("The max temperature is:", maximum_temperature)
#Lowest temp print
min_temperature = min(Temperatures)
print("The minimum temperature is:", min_temperature)