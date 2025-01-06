# Question 1
student = {"name": "Alice",
           "age": 20,
           "major": "Computer Science"}
print(student)

# Question 2
person = {"name": "John",
          "age": 25,
          "city": "New York"
          }
print(person.get("city"))

# Question 3
car = {"brand": "Toyota",
       "model": "Corolla"
       }
car.update({"year": 2020})
print(car)

# Question 4
book = {"title": "Python Basics",
        "price": 15.99
        }
book["price"] = 12.99
print(book)

# Question 5
inventory = {"apples": 10,
             "bananas": 5,
             "oranges": 8
             }
inventory.pop("bananas")
print(inventory)

# Question 6
grades = {"Alice": 85,
          "Bob": 90,
          "Charlie": 78
          }
for key, value in grades.items():
    print(key, ":", value)

# Question 7
user = {"username": "admin",
        "password": "1234",
        }
if "email" in user:
    print("Key exists")
else:
    print("Key does not exist")

# Question 8
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

# Question 9
course = {"name": "Python",
          "level": "Beginner",
          "duration": "3 months"
          }
my_keys = course.keys()
my_values = course.values()
print(my_keys)
print(my_values)

# Question 10
words = ["apple", "banana", "orange", "banana", "apple"]
count_words = {}
for item in words:
    if item in count_words:
        count_words[item] += 1
    else:
        count_words[item] = 1
print(count_words)

# Question Bonus Challenge
scores = {"Alice": 90,
          "Bob": 80,
          "Charlie": 95
          }
highest_scores = max(scores)
for item in scores:
    if item == highest_scores:
        print(scores[item])
