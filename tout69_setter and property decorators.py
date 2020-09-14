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
        self.fname=None
        self.lname=None

obj1 = Employee("jitendra", "khadka")
obj1.fname = "jitu"
obj1.lname = "ji"
print(obj1.fname)
obj1.email = "jitendra.khadka4@gmail.com "
del obj1.email
print(obj1.email)
obj1.email="jitenra.khadka@nishanaweb.com"
print(obj1.email)

