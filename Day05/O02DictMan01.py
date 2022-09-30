
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print('-' * 40)
d2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(f'd2 :{d2}')
print(type(d2))

print('-' * 40)
d3 = dict([('name', 'sachin'), ('runs', 125), ('oppn', 'Aus'), ('venue', 'SCG')])
print(f"d3 :{d3}")
print(type(d3))

print('-' * 40)
d4 = dict(name="rahul", runs=85, oppn="SA", venue="dublin")
print(f"d4 :{d4}")
print(type(d4))

print('-' * 40)

#read
player = {'name': 'rahul', 'runs': 85, 'oppn': 'SA', 'venue': 'dublin'}
print(f"Name :{player['name']}")
print(f"Opponent :{player['oppn']}")

print('-' * 40)
# iterate
for x in player:
    print(x, "=>", player[x])

# modification
print('-' * 40)
print(f"player :{player}")
player['ply2'] = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'SCG'}

print('-' * 40)
print(f"player :{player}")

print('-' * 40)
for x in player:
    if isinstance(player[x], dict):
        print("-" * 40)
        for y in player[x]:
            print(y, "=>", player[x][y])
    else:
        print(x, "=>", player[x])

player['runs'] = 102
player['oppn'] = 'Zimbabwe'

print(f"player :{player}")

# del
del player['oppn']
del player['venue']

print("-" * 40)
print(f"player :{player}")

print("-" * 40)
print(dir(player))
