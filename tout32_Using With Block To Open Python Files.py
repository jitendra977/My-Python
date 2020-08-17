with open("file_test.txt") as f:
    a = f.readlines()
    print(a)
# Yes run this system
f = open("file_test.txt")
a = f.read()
print(a)
f.close()
# f being the object of the file. The important thing to note is, there is no close() function required. After
# running the code in the block, the file will automatically be closed.