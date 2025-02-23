employees = [
 {"name": "Alice", "department": "Sales", "salary": 45000},
 {"name": "Bob", "department": "Engineering", "salary": 60000},
 {"name": "Charlie", "department": "Marketing", "salary": 40000},
 {"name": "Diana", "department": "Engineering", "salary": 70000},
 {"name": "Eli", "department": "Sales", "salary": 55000},
 {"name": "Frank", "department": "Engineering", "salary": 60000},
]
# 1
high_earners = [x for x in employees if x["salary"] >= 50000]
print(high_earners)

# 2
sorted_employees = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
print(sorted_employees)

for x in sorted_employees:
 print(f"{x['name']}: ${x['salary']}")

# 3
engineering_payroll = sum(emp["salary"] for emp in employees if emp["department"] == "Engineering")

print(f"Total Engineering Payroll: ${engineering_payroll}")

# 4
highest_salary = max(employees, key=lambda emp: emp["salary"])
print("HIGHEST SALARY")
print("----------------")
print(highest_salary)

# 5
department_groups = {}
for emp in employees:
    dept = emp["department"]
    if dept not in department_groups:
        department_groups[dept] = []
    department_groups[dept].append(emp)

print("----------------------")
print("GROUPED BY DEPARTMENT")
print("----------------------")
print(department_groups)