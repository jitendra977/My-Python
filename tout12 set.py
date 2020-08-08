set={1,2,3,4,5}
print(type(set))
fruits = {"apple", "banana", "cherry"}
#Add element in set
# syntax  set.add(elmnt)
fruits.add("mango")
# set difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.difference(y)
za=x-y
# union
u=x.union(y)
# symmetric difference
sd = x.symmetric_difference(y)

i=x.intersection(y)
print("union:",u)
print("difference:",z)
print("Intersection",i)
print("sd:",sd)