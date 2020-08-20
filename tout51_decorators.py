def inner(func):
    def inner2():
        print("---------before for executions--------------")
        func()
        print("---------after func execution----------------")
    return inner2
@inner
def inside_func():
    print("this is the inside of func")
inside_func()
