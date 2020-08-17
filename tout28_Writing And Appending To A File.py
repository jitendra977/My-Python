# f = open("file_test.txt", "w")
# # w mode remove old text
# a = f.write("\nthis is the write test for open file writing mode")
# print(a)
#
# f = open("file_test.txt", "a")
# # a mode add new text with old text
# a = f.write("\nthis is the write test for open file writing mode")
# print(a)

# hanle read and write mode
f = open("file_test.txt", "r+")
print(f.read())
f.write("\nthis text form r+ mode")
print(f.read())