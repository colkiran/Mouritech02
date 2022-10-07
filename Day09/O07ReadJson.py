
import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print('=' * 40)

print("-" * 40)
# data should be enclosed in single quotes
empdata = '{"name": "Mike", "age": 29, "city": "Melbourne"}'
print(empdata)
print(type(empdata))

# convert this string into python dictionary
res = json.loads(empdata)
print(res)
for k in res:
    print(k, "=>", res[k])


# load  =   used to read the JSON document from a file
# loads =   used to convert JSON string document into python dictionary