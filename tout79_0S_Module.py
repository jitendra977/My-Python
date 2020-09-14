import os

print(dir(os))
print(os.getcwd())
f = open('file_test.txt')
os.chdir(r"E:\Project\Elegoo Smart Robot Car Kit V2.0")
print(os.getcwd())
print(os.listdir(r"C:\Users\jiten\PycharmProjects\Myfirstprog\My-Python\JITU"))
os.chdir(r"C:\Users\jiten\PycharmProjects\Myfirstprog\My-Python\JITU")
os.mkdir("My_FILE/hello")
# os.rename("File_2_29-Aug-2020.txt", "My_file.txt")
print(os.environ.get(r"C:\Users\jiten\PycharmProjects\Myfirstprog\My-Python\JITU"))
