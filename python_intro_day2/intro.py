def f1(a,s,d):
    print(a)
    print(s)
    print(d)
    return a*s*d
result = f1(1,2,3)
print(result)
#****************Lamda Function********************
f2 = lambda arg1,arg2:arg1+arg2
print(f2(2,3))
#**************function returning a lambda function************
def f3(arg1):
    arg1+=arg1
    print(arg1)
    return lambda arg1:arg1+arg1
print(f3(5)(5))                
