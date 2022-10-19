
import time
from datetime import datetime
import pytz

curtime = time.localtime()
print(f"curtime :{curtime}")
print("time is :", time.strftime("%H : %M : %S", curtime))

print("-" * 40)
tm1 = "9:32:56"
tm2 = "18:45:10"

print(f"tm1 :{tm1}")
print(type(tm1))

print("-" * 40)
print(f"tm2 :{tm2}")
print(type(tm2))

t1 = datetime.strptime(tm1, "%H:%M:%S")
print(f"Login time :{t1}")
print(type(t1))

print("-" * 40)
t2 = datetime.strptime(tm2, "%H:%M:%S")
print(f"Login time :{t2}")
print(type(t2))

print("-" * 40)
result = t2 - t1

print(result)
