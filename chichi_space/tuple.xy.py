# Tuple

my_tuple = (3, 4, 5)

first_element = my_tuple[0]

my_list = [3, 4, 5, 3]


tp = tuple(my_list)

print(my_list)
print(tp)


months = ["January", "February", "June", "March", "April", "May", "June", "July"]


#Membership

answer = months.index("June")
print(answer)

d = {
    "name": ["Kindson", "Munonye", "Joe"],
    "Location": ["Budapest", "USA", "Canada"]
}



#Tuple packing and unpacking

my_tuple = ("Jonn Doe", 78.3, "Computer Science, ""A" )

full_name, score, department, grade = my_tuple   #unpacking