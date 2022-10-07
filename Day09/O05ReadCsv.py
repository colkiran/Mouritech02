
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    empTbl = PrettyTable(next(emp_details))

    # colname = next(emp_details)             # emp_details.__next__
    # print(*colname)

    for rec in emp_details:
        # print(*rec)
        empTbl.add_row(rec)

print(empTbl)
