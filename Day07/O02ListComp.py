
squares = [x ** 2 for x in range(1, 11)]
print(squares)
print("-" * 40)

fruits = [
    ("apples", 280),
    ("orange", 110),
    ("grapes", 135),
    ('pineapple', 80),
    ('banana', 70),
    ('gauva', 85),
    ('pears', 180),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 40)

prices = ["fruit" for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit[0] for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit[1] for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit[1] * 0.9 for fruit in fruits]    # discount of 10%
print(prices)
print("-" * 40)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(prices)
print("-" * 40)

prices = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75] for fruit in fruits]
print(prices)
print("-" * 40)

expnFrts = [fruit for fruit in fruits if fruit[1] > 100]
print(expnFrts)
print("-" * 40)

prices = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75] for fruit in fruits if fruit[1] > 100]
print(prices)
print("-" * 40)

sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
res = [word for word in sentence.split()]
print(res)
print("-" * 40)

words = [word for word in sentence.split() if word != "the"]
print(words)
print("-" * 40)

words = [(word, len(word)) for word in sentence.split() if word != 'the']
print(words)

print("-" * 40)
boys = ['sachin', 'rohit', 'rahul', 'virat', 'yuvraj', 'dhoni']
girls = ['deepika', 'sonam', 'alia', 'shradha', 'katrina', 'kareena']

combine = [(boy, girl) for boy in boys for girl in girls]
print(combine)
print("-" * 40)

combine = list(zip(boys, girls))
print(combine)
