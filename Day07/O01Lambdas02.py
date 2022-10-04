
l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

# conversions - currency - from rs to dollar, weights -> kgs  to pounds
            # temperature - from cel to faren

months= ['aug', 'apr', 'dec', 'jul', 'sep', 'jan','oct', 'feb', 'jun', 'nov', 'mar', 'may' ]

from calendar import month_name

res_asc = sorted(months, key=list(map(lambda mth: mth[0:3].lower(), list(month_name))).index)
print(f"months :{months}")
print(f"Asc    :{res_asc}")

print("filter".center(40, "-"))
l = list(range(1, 26))
print(f"l :{l}")

res = list(filter(lambda x : x % 3 == 0, l))
print(res)

sentence = "the quick brown fox jumps over the lazy dog"
words = list(filter(lambda word: word != 'the', sentence.split()))
print(words)

print("reduce".center(40, "-"))
from functools import reduce
l = [3, 7, 6, 4, 8, 5, 9, 2, 10]

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x if x < y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")
