# Encapsulation 

class A:
    def __init__(self,a,b):
        self._a = a # protected 
        self._b = b # protected 

class B(A):
    def showA(self):
        a = A(20,30)
        print(a._a)

obj = B(10,20)    
obj.showA()


# print(obj.a) # not accessible 
# print(obj.b) # not accessible 