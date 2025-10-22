# Encapsulation 

class A:
    def __init__(self,a,b):
        self.__a = a # private  
        self.__b = b # private  

obj = A(10,20)    

print(obj.a) # not accessible 
print(obj.b) # not accessible 

# print(obj._A__a) # accessing via name mangling 
# obj._MyClass__private_variable