try:
    fp = open("filerename.py")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()