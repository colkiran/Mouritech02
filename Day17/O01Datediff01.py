
from datetime import datetime

dt = datetime.now()
print(f"dt :{dt}")

print("-" * 40)
print(f"Day :", dt.strftime("%a"))
print(f"Day :", dt.strftime("%A"))

print("-" * 40)
print(f"Month :", dt.strftime("%b"))
print(f"Month :", dt.strftime("%B"))

print("-" * 40)
print(f"date :", dt.strftime("%d"))
print(f"date :", dt.strftime("%D"))
print(f"date :", dt.strftime("%x"))

print("-" * 40)
print(f"year :", dt.strftime("%y"))
print(f"year :", dt.strftime("%Y"))

print("-" * 40)
print(f"time :", dt.strftime("%T"))
print(f"time :", dt.strftime("%X"))

print("-" * 40)
dt1 = dt.strftime("%d-%m-%y")
print(f"dt1 :{dt1}")

print("-" * 40)
dt2 = dt.strftime("%d-%m-%Y")
print(f"dt2 :{dt2}")

print("-" * 40)
dt3 = dt.strftime("%d-%b-%Y")
print(f"dt3 :{dt3}")

print("-" * 40)
dt4 = dt.strftime("%d-%B-%Y")
print(f"dt4 :{dt4}")

print("dt1 :", type(dt1))
print("dt2 :", type(dt2))
print("dt3 :", type(dt3))
print("dt4 :", type(dt4))
