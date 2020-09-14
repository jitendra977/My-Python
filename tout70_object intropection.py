class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"The Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is Not set"
        return f"{self.fname}.{self.lname}@nishanaweb.com"

    @email.setter
    def email(self, string):
        print("Setting Now....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


obj1 = Employee("jitendra", "khadka")
a = "this is the strint "
print(dir(obj1))
print(id(obj1))
import inspect

print(inspect.getmembers(obj1))
