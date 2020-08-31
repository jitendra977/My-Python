class Student:
    _name = "Dandabir"  # Privet var
    roll = 10  # class var
    __branch = "Nepal"  # Protected Var

    def __init__(self, name, roll):
        self.name = name
        self.role = roll

    def _displayname(self):
        print("Name", self._name)
        print("Roll:", self.roll)
        print("Bracnh:",self.__branch)


d = Student("ram", 55)
d._displayname()
print(d.name)
print(d._Student__branch)