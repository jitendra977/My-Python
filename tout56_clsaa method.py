class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


ram = Employee("Ram bahadur Thapa", 5000, "Manager")
ram.change_leaves(30)
print(ram.no_of_leaves)