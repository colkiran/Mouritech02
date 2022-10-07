
FL = open("data.txt", "rb")

print(f"Position :{FL.tell()}")

pos = FL.seek(35, 0)
print(f"Position :{pos}")

pos = FL.seek(65, 1)
print(f"Position :{pos}")

pos = FL.seek(-200, 2)
print(f"Position :{pos}")

FL.close()