mydics={"name":"Ankit",
"age":30,
"Address":{
   "city": "hyderabad",
   "pin":480015
}
}
print(mydics)
print(len(mydics))
print(mydics["Address"]["city"])
mydics2= dict(company="ATMCS technology hyderabad",salary=450000.4)
print(mydics2)
mylist = list((1,2,3,mydics,mydics2))
print(mylist)
for x in mylist:
    
    if(type(x)==dict):
        print(len(x))
    print("x : ",x)
    print(type(x))