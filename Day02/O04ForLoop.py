
for i in range(1, 6):
    print("hello")

print("-" * 40)

for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 25, 2):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 25):
    if i % 2 == 0:
        print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 25):
    # if i > 20:
    #     break
    if i % 2 == 1:
        continue                # skip the iteration
    print(i, end=" ")
else:
    print("\niteration completed.....")