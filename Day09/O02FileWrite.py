
"""
write mode
----------
if the exists then first deletes the contents of the file and then writes newly into the file.

if the file does not exist then creates a new file and then writes into the file

"""


FW = open("myfile.txt", "w")

# st = input("Enter the contents of the file :")
# FW.write(st)

line1 = "This is the first line. \n"
line2 = "This is the second line. \n"
line3 = "This is the third line. \n"

FW.writelines([line1, line2, line3])

FW.close()