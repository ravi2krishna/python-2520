# Encapsulation 

class A:
    def __init__(self,a,b):
        self.a = a # public 
        self.b = b # public 

obj = A(10,20)    

print(obj.a) # accessible 
print(obj.b) # accessible 