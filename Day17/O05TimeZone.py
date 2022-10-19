"""
utc - universal time coordinates

"""
from datetime import datetime
import pytz
import time

curtime = time.localtime()
curclock = time.strftime("%H:%M:%S", curtime)
print(curclock)

print("-" * 40)
utc = pytz.utc
print(f"utc :{utc}")

print("-" * 40)
IST = pytz.timezone('Asia/Kolkata')
print(f"IST :{IST}")

print("-" * 40)
print("utc default format :", datetime.now(utc))

print("-" * 40)
print("ist default format :", datetime.now(IST))

print("-" * 40)
IST = pytz.timezone('Asia/Kolkata')
NYT = pytz.timezone('America/New_York')
UKT = pytz.timezone('Europe/London')
AST = pytz.timezone('Australia/Melbourne')

print("Indian Time          :", datetime.now(IST))
print("American Time        :", datetime.now(NYT))
print("United Kingdom Time  :", datetime.now(UKT))
print("Australian Time      :", datetime.now(AST))
