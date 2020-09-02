class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetail(self):
        print(f"Name:{self.name}   Salary:{self.salary}   Role:{self.role}")

    def __add__(self, other):
        return self.salary + other.salary

    def __str__(self):
        print({self.name}, {self.salary}, {self.role})

    def __repr__(self):
        print(self.name, self.salary, self.role)


emp1 = Employee("RamBahadur", 8000, "Manager")
emp2 = Employee("Hari", 5000, "Director")
emp1.printdetail()
print(emp2 + emp1)
print(str(emp1))
