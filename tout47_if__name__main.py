def printer(string):
    return "Hello world " + string


def add(n1, n2):
    return n1 + n2 + 5


print("add he name is:", __name__)
if __name__ == '__main__':
    print(printer("hi "))
    a = add(3, 5)
    print(a)
