file = open("example.txt", "w")

file.write("Hello World\n")

file.close()

file2 = open("example.txt", "r")
for line in file2:
    print(line.strip())
file2.close()

