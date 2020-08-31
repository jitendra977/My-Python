class Student:
    __name = None
    __roll = None
    __branch = None

    def __init__(self, name, roll):
        self.name = name
        self.role = roll

    def __displayname(self):
        print("Name", self.__name)
        print("Roll:", self.__roll)
d = Student("ram",55)
d.name



