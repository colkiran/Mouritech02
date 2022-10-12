

import sys
#
# sys.path.append("C:\\Delhi")
#
for pth in sys.path:        # sys.path is a list
    print(pth)

from gurgaon.mymodule import Product, greet, sum, runs

prd1 = Product("Lays", 30)
print(prd1.get_details())

print("-" * 40)
prd2 = Product("Kur Kure", 25)
print(prd2.get_details())

print("-" * 40)
greet("Mahendra Singh Dhoni")

print(sum(340, 524))

print(runs)
