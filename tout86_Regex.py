# import re
# text = "Hello world "
# y = re.findall("^hello",text)
# if text :
#     print('yes find item ')
# else:
#     print("No match item")
import re
txt = "hello world "
x = re.findall("world$",txt)
if txt:
    print("Yes string end with world")
else:
    print("No match found")