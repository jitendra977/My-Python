# list comprehensions
lst = [i for i in range(100) if i % 3 == 0]
print(lst)
# dictionary  comprehensions
dict1 = {i: f'item{i}' for i in range(1, 100) if i % 20 == 0}
dict2 = {value: key for key, value in dict1.items()}
print(dict1)
print(dict2)
# set comprehensions
dress = {dress for dress in ['dress1', 'dress2', 'dress3', 'dress1', 'dress2', 'dress3']}
print(dress)
# Generator
even = (i for i in range(100) if i % 20 == 0)
print(even.__next__())
print(even.__next__())
