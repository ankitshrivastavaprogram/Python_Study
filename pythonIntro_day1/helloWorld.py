
""" this is 
multyple line comand  """

print("hello world")
if(5>7):
    print("5 is greater then 2")
else :
    print("printing else part")
#comments in python
x=12
print("x= ",x)#print("x="+x) will give us a error
x="ankit"
print("x="+x)

#thre three types of number in python
#int   float   complax
x=12
print(type(x))
x=12.5
print(type(x))
x=12j
print(type(x))

#python castingcast
print("**********python cast ****************")
x=int(12)
print("type(",x,")",type(x))

x=int("12")
print("type(",x,")",type(x))

x=float("12")
print("type(",x,")",type(x))

x=str(12)
print("type(",x,")",type(x))

x=str(12.01)
print("type(",x,")",type(x))

#*********command line string input********************
print("enter your name :")
name = "input()"
print("enter your age :")
age="input()"
print("name: ",name," age : ",age)

#*****************List *****************************
l1 = [1,2,3,4,5]
print(l1)
l2=[1,2,"ankit","12.5",12.8,12j]
print(l2)
print(l2[2:4])
l1.append(l2)
print(l1)
l3=list((1,2,3,4,"raja"))
print(l3)
print(len(l3))

#******************Touple*********************************
print("**************Touple*********************")
t1=(1,2,3,4.7,"string",12j)
print(t1)
print(len(t1))





