class A:
    classVar = "Im in a class var A "

    def __init__(self):
        super().__init__()
        self.var1 = "i m in a class constructor A"
        self.classVar = "I m in a Instance Variable A  "


class B(A):
    classVar = "Im in a class variable B "

    def __init__(self):
        self.var1 = "i m in a class constructor B  "
        self.classVar = "I m in a Instance Variable B"
        super().__init__()


a = A()
b = B()
print(b.classVar, b.classVar, a.classVar)
