# F strings
import math

me = "JITU"
a1 = 3
a12 = "this is %s %s"%(me, a1)
a = "This is {1} {0}"
b = a.format(me, a1)
print(b)
print(a1)
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)

