n = 5
if n == 5:
    print(r"Hello This is ==5")
# if n is 5:
# print("hey")


a = [1, 3, 4, 2, 4, 5, 2, ]
b = a
print(b is a)  # True
print(b == a)  # True
b = a[:]
print(b is a)  # False
print(b == a)  # True
