def gen(n):
    for i in range(n):
        yield


g = gen(3)
print(g.__next__())
print(g.__next__())
