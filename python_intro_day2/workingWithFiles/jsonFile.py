import json
mydict = {
     "name":"Ankit Shrivastava",
      "age":30
}



f =open("jsonData","r")
str2=f.read()
l2=json.loads(str2)
l2.append(mydict)
print(l2)
f.close()
f =open("jsonData","w")
f.write(json.dumps(l2))
