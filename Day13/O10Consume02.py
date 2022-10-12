
import mypackage.mymodule as m
from mypackage.mymodule import Product, sum

print(sum(550, 765))
m.greet("Kapil Dev")

print("-" * 40)
p1 = Product('Dairymilk', 40)
p1.get_details()

print("-" * 40)
p2 = Product('KitKat', 55)
p2.get_details()