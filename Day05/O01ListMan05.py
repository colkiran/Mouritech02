
print("sort".center(40, "-"))
l = [8, 5, 1, 9, 6, 3, 10, 4, 7, 2]
print(f"l :{l}")

print("-" * 40)
res = sorted(l)
print(f"Ascending  :{res}")

l.sort(reverse=True)
print(F'Descending :{l}')

print("-" * 40)
print()
l = [8,'zebra', 'apple',  5, 'yellow', 'blue', 1, 'white', 'green',  9, 'violet', 'maroon', 6, 'purple', 'red', 3, 'xmas', 'cat', 10, 'dog', 'egg', 4, 'hen', 'ink', 7, 2, 185, 1564, 28, 267, 2015, 37, 345, 3210]

print(f"l :{l}")

print("-" * 40)
print()

res = sorted(l, key=ascii)
print(f"res :{res}")

print("-" * 40)
print()

cities = ['thiruvananthapuram', 'chennai', 'bangalore', 'hyderabad', 'ooty', 'delhi',
          'vishakapatnam', 'mumbai', 'pune', 'kanyakumari', 'mysore']
print(f'cities :{cities}')

print("-" * 40)
print()

res_asc = sorted(cities, key=len)
print(f"Ascending :{res_asc}")

print("-" * 40)
print()

res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 40)
print()

months= ['aug', 'apr', 'dec', 'jul', 'sep', 'jan','oct', 'feb', 'jun', 'nov', 'mar', 'may' ]

# sort this list by calendar

from calendar import month_name
print(f"month_name :{list(month_name)}")

calmonth = []
for mth in list(month_name):
    calmonth.append(mth[0:3].lower())

print("-" * 40)
print()

def sort_months(mon):
    if mon in calmonth:
        return calmonth.index(mon)

print(f'months :{months}')

res_asc = sorted(months, key=sort_months)
print(f"Asc   :{res_asc}")

res_desc = sorted(months, key=sort_months, reverse=True)
print(f"Desc  :{res_desc}")

print("reverse".center(40, "-"))
l = [8, 5, 1, 9, 6, 3, 10, 4, 7, 2]
print(f"l :{l}")

l.reverse()

print(f"l :{l}")
