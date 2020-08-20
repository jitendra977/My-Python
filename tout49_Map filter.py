#map(function,iterable)>> each itreable list tuple return of reasult
item=[1,2,3,4,5,6,7,8,9,10]
a=list(map((lambda x:x**2),item))
print(a)
#filter(function,iterable) >> which itrable function is true
a=[1,2,3,4,5,6,7]
b=[2,4,5,7,5,2,12,11,10]
c=list(filter(lambda x:x in a,b))
print(c)
# reduce(function,iterable)
from functools import reduce
a = reduce((lambda x,y:x*y),[1,2,3,4])
print(a)