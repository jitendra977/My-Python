class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @staticmethod
    def printgood(string):
        print("This is good" + string)


ram = Employee("Ram bahadur", 6000, "manager")
Employee.printgood("  Ram")
