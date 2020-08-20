class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


ram = Employee("Ram bahadur Thapa", 5000, "Manager")
shushil = Employee.from_dash("Shushil KC-3000-Helper")
print(shushil.salary)
print(shushil.__dict__)