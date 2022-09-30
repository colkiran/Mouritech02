
emp = {
    'emp1':{'empname': 'Melvin', 'age': 32, 'dept': 'finance', 'desig': "MGR", 'loc': 'che', 'sal': 85000},
    'emp2':{'empname': 'Tina', 'age': 38, 'dept': 'MKT', 'desig': "BDM", 'loc': 'Del', 'sal': 75000},
    'emp3':{'empname': 'Moses', 'age': 29, 'dept': 'IT', 'desig': "Sft Eng", 'loc': 'Pun', 'sal': 125000}
}

print("-" * 40)
print(f"emp :{emp}")

print("-" * 40)
print(f"emp1 :{emp['emp1']}")
print("-" * 40)
print(f"emp2 :{emp['emp2']}")
print("-" * 40)
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'empname': 'Melvin', 'age': 32, 'dept': 'finance', 'desig': "MGR", 'sal': 85000}
emp2 = {'empname': 'Tina', 'age': 38, 'dept': 'MKT', 'desig': "BDM", 'loc': 'Del'}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(40, "-"))
emp1 = {'empname': 'Melvin', 'age': 32, 'dept': 'finance', 'desig': 'MGR', 'sal': 85000}
print(f"emp1 :{emp1}")
emp1.clear()

print(f"emp1 :{emp1}")
