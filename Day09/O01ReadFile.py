
"""

read mode - this is the default mode, if the file exists then it opens the file for reading. if the file does not exist then throws an error message

read()  - by default reads the entire contents of the file, if the bytes are mentioned then reads the specified no of bytes from the file.

readline() - reads one line at a time. bytes mentioned should be less than or equal to the size of the line

readlines() - will read all the lines and stores it in a list, we can iterate the list. if the bytes are mentioned then checks in which line the byte exists and prints data from the beging to end the of the current line

"""

FL = open("data.txt", "r")

# st = FL.read(100)
# st = FL.readline(852)
# print(st)

st = FL.readlines(950)
print(st)
# for line in st:
#     print(line)

FL.close()