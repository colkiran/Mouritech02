
def addme(x, y):
    return x + y

a = addme
print(a(10, 20))

print("-" * 40)

b = lambda a, b: a + b
print(b)
print(type(b))

print(b(100, 200))

# lambdas are best used with other functions like - map, filter and reduce
# map    - lambda expression is executed on all values of a list

# filter - lambda expression will return a True or a False, filter will implement
#          this expression on all values in a list and return those values which
#          returns a True

# reduce is imported from functools
# reduce - will convert the given list into a single value
