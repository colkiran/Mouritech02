
player = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'SCG', 'age': 31, 'year': 2001}
print(f"player :{player}")
print("-" * 40)

print(player.get('name', "Please enter a valid key"))
print(player.get('gender', "Please enter a valid key"))

print("setdefault".center(40, "-"))
# used add only new key value pairs
player = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'SCG'}
print(f"player :{player}")
print("-" * 40)

player.setdefault('name', "tendulkar")
player.setdefault('runs', 150)
player.setdefault('age', 31)
player.setdefault('year', 2001)

print(f"player :{player}")

print("keys".center(40, "-"))
player = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'SCG', 'age': 31, 'year': 2001}
print(f"player :{player}")

print("-" * 40)
k = player.keys()
print(k)
print(type(k))

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))

player = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'SCG', 'age': 31, 'year': 2001}
print(f"player :{player}")

print("-" * 40)
v = player.values()
print(f"v :{v}")
print(type(v))

print("fromkeys".center(40, "-"))
# convert a list into a dictionary, elements of the list will become dictionary keys

cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol', 'pun']
print(f"cities :{cities}")

print("-" * 40)
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("pop".center(40, "-"))

player = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'SCG', 'age': 31, 'year': 2001}
print(f"player :{player}")

print("-" * 40)
res1 = player.pop("runs")
print(f"res1 :{res1}")

print("-" * 40)
res1 = player.pop("venue")
print(f"res1 :{res1}")

print("popitem".center(40, "-"))

player = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'SCG', 'age': 31, 'year': 2001}
print(f"player :{player}")

print("-" * 40)

res1 = player.popitem()
res2 = player.popitem()

print(f"res1 :{res1}")
print(f"res2 :{res2}")
