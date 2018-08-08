class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showMyInfo(a,a2):
        a.age+=a2
        print("name ",a.name," age ",a.age," increcer : ",a2)
obj = A("ankit",30)
obj.showMyInfo(12)            
