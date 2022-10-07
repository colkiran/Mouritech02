FA = open("myfile.txt", "a")

i = 1
while (i):
    st = input("Enter the contents of the file:")
    FA.write(st + "\n")
    st = input("Do you wish to continue :")
    if st == 'NO':
        i = 0
    else:
        i = 1

FA.close()