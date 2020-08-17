f = open("file_test.txt")
f.seek(0)#File pointer find
print(f.tell())#Tell the file pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

