print("Hello How are you My dictonary")
dic={"Banana":"Banana is a yellow fruit","Apple":"Apple is a Red Fruit","Orange":"Orange is a Yello Fruit"}

for x in dic: #Print all key names in the dictionary
    print(x)

#Print all values in the dictionary, one by one:
for x in dic:
    print(dic[x])

#Loop through both keys and values, by using the items() method:
for x,y in dic.items():
    print(x,":",y)

#Check if "Banana" is present in the dictionary:
if "Banana" in dic:
  print("Yes, 'Banana' is one of the keys in the 'DIC' dictionary")

#Print the number of items in the dictionary:
print(len(dic))

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
dic["grape"]="Grape is blue color"
print(list(dic))





c = {"child1" : {"name" : "Emil", "year" : 2004},"child2" : {"name" : "Tobias","year" : 2007 },"child3" : {"name" : "Linus","year" : 2011}}
print(list(c))
print(c.get("child1",))



# a = {'key', 'value', 'cow':'mooh'}
# print(a)
#will print "mooh" on the screen
# Dictionary is nothing but key value pairs
# d1 = {}
# print(type(d1))
# d2 = {"Harry":"Burger",
#       "Rohan":"Fish",
#       "SkillF":"Roti",
#       "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# print(d2)
# del d2[420]
# print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(dic.items())
