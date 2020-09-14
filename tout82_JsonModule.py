import json

# some JSON:
x = '{ "name":"Jitendra khadka",' \
    ' "age":27, ' \
    '"Address":"Rukum Nepal",' \
    '"Current":"Sendai Japan"}'

# parse x:
y = json.loads(x)
z = json.dumps(x)
# the result is a Python dictionary:
print(y["Address"])
print(z)
