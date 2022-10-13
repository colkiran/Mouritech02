
import mouritech02_package_root.mouritech02 as m
from mouritech02_package_root.mouritech02 import Product

m.greet("Zaheer Khan")

print("-" * 40)
p1  = Product("Pepsi", 35)
p1.get_details()

print("-" * 40)
p1  = Product("Coke", 25)
p1.get_details()

print(m.sum(200, 780))