class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role


ram = Employee("Ram bahadur Thapa", 5000, "Manager")
hari = Employee("Haribansha Achrya", 8000, "Instructor")
print(hari.name)