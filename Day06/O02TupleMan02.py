
from collections import namedtuple

nmdTpl = namedtuple("Products", "pname, price, qty, cat")
prod = nmdTpl(pname="Pepsi", price=85, qty=15, cat="Baverage")

print(prod)
print(f"Name     :{prod.pname}")
print(f"Price    :{prod.price}" )
print(f"Quantity :{prod.qty}")
print(f"Category :{prod.cat}")

prod.pname = "Coke"
