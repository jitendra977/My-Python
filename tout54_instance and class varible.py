class Employee:
    no_of_leaves=8
    pass
ram = Employee()
hari = Employee()
ram.name = "Ram Bahadur Thapa"
ram.salary = 1000
ram.role = "Manager"
hari.name = "Hari Bansa Achrya"
ram.salary = 5000
ram.role = "Instructor"
print(Employee.no_of_leaves)
print(hari.no_of_leaves)
print(ram.__dict__)
Employee.no_of_leaves=10
print(Employee.no_of_leaves)
print(ram.no_of_leaves)