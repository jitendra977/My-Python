class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetail(self):
        return f"My name is:{self.name}and My Salary is {self.salary},Working in{self.role}"


class Player:
    no_of_leaves = 15

    def __init__(self, game):
        self.game = game

    def printdetail(self):
        print(self.game)


Hari = Player("Vollyball")
print(Hari.game)

