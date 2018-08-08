import json
import datetime
mydict = {
    "name":"ankit",
    "age":12
}
print(type(mydict))
x= json.dumps(mydict)
print(type(x))
y= json.loads(x)
print(y["name"])