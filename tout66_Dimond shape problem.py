class A:
    def meet(self):
        print("Method from class A ")


class B(A):
    def meet(self):
        print("Method from class B ")


class C(A):
    def meet(self):
        print("Method from class C ")


class D(C, B):
    def meet(self):
        print("Method from class D ")


a = A()
b = B()
c = C()
d = D()
d.meet()
