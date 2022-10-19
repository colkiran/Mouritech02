
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")

itrObj = iter(l)

while True:
    try:
        elem = next(itrObj)
        print(elem, end=" ")
    except StopIteration:
        break
print()

print("-" * 40)
for i in l:
    print(i, end=' ')
print()
