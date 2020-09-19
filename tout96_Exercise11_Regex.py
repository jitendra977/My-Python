import re

with open("email.txt")as f:
    str = f.read()
email = re.findall(r"[a-zA-Z0-9._-]+@+[a-zA-Z]+\.+[A-Za-z]+", str)
print(email)
