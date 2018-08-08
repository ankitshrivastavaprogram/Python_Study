import os
#print(dir(os.path))
f= open("newFile","at")
f.write("this is new line 1")
f.write("this is new line 2")
#print(dir(f))
f.close()
f=open("newFile","r")
for line in f:
    print(line)