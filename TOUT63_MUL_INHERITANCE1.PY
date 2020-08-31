class Student:
    def __init__(self):
        self.name = input("Enter our Name")
        self.cname = input("Enter Your Collage Name:")
        self.roll = input("Enter Your Roll No:")
        self.marks = int(input("Enter your marks:"))


class Test(Student):
    def Check(self):
        if self.marks > 60:
            print("You Valid for next level.")
        else:
            print("You can not process for next level.")


class Admin(Test):
    def Display(self):
        print("=========STUDENT INFO=========")
        print(f"Name:{self.name}")
        print(f"College:{self.cname}")
        print(f"Roll:{self.roll}")


obj = Admin()
obj.Display()
