class parent:
    def parent(self):
        print("Parent Function")


class child(parent):
    def child(self):
        print("We are inside the child")


child = child()
child.parent()
