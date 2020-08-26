class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetail(self):
        return f"My name is:{self.name}and My Salary is {self.salary},Working in{self.role}"


class programmer(Employee):
    no_of_leaves = 10

    def __init__(self, name, salary, role, language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language


Ram = Employee("Ram Bahadur", 6000, "Admin")
Hari = programmer("hari bansha", 5000, "Programmer", ["python", "HTML", "Java"])
print(Hari.language)
