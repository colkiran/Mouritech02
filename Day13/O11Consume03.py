
import sys

sys.path.append("C:\\Delhi")

for pth in sys.path:        # sys.path is a list
    print(pth)

from gurgaon.mymodule import Product, greet, sum, runs

prd1 = Product("Good Day", 30)
print(prd1.get_details())

print("-" * 40)
prd2 = Product("Hide n Seek", 45)
print(prd2.get_details())

print("-" * 40)
greet("Yuvraj Singh")

print(sum(15, 80))

print(runs)
