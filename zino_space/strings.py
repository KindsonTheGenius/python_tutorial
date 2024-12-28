# Question 1
text = "Hello, Python!"
print(len(text))

# Question 2
str1 = "Hello"
str2 = "World"
str = str1 + " " + str2
print(str)

# Question 3
text1 = "Python"
print(text1[3])

# Question 4
text2 = "Python Programming"
print(text2[7:])

# Queston 5
lower_text = "hello world"
upper_text = "HELLO WORLD"
print(lower_text.upper(), upper_text.lower())

# Question 6
text3 = "apple pie and apple tart"
print(text3.count("apple"))

# Question 7
text4 = "I love Python programming"
for i in text4:
    if "Python" in text4:
        print("Text exists")
        break
    else:
        print("Text does not exist")

# Question 8
text5 = "Python"
print(text5[::-1])

# Question 9
text6 = "The cat sat on the mat with another cat"
new_text = text6.replace("cat", "dog")
print(new_text)

# Question 10
text7 = "Python is fun"
list(text7)
joined = "-".join(text7)
print(joined)
