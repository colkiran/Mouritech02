
from datetime import datetime
import dateutils

dt1 = "Wednesday, September 30, 2020"
print(f"dt1 :{dt1}")
print(type(dt1))

print("-" * 40)
dt2 = "Sunday, October 31, 2021"
print(f"dt2 :{dt2}")
print(type(dt2))

print("-" * 40)
actd1 = datetime.strptime(dt1, "%A, %B %d, %Y")
print(f"actd1 :{actd1}")
print(type(actd1))

print("-" * 40)
actd2 = datetime.strptime(dt2, "%A, %B %d, %Y")
print(f"actd2 :{actd2}")
print(type(actd2))

print("-" * 40)
print("No of days :", actd2 - actd1)

print("-" * 40)
print("Difference in no of day :", dateutils.days(actd2, actd1))

print("-" * 40)
print("Difference in no of weeks :", dateutils.weeks(actd2, actd1))

print("-" * 40)
print("Difference in no of months :", dateutils.months(actd2, actd1))

print("-" * 40)
print("Difference in no of years :", {round(dateutils.years(actd2, actd1), 2)})
