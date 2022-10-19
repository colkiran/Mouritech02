
from datetime import datetime
import timeutils

login_time = datetime.strptime("9:32:56", "%H:%M:%S")
logout_time = datetime.strptime("18:45:15", "%H:%M:%S")

print(f"Login  :{login_time}")
print(f"Logoff :{logout_time}")

delta = logout_time - login_time

print("-" * 40)
sec = delta.total_seconds()
print(f"Total time in Seconds :{sec}")

min = round(sec / 60, 0)
print(f"difference in Minutes :{min}")

hours = round(sec / (60 * 60), 2)
print(f"difference in Hours :{hours}")