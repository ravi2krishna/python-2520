# Traditional Overloading
class MathOps:
    
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c): # overwrites the above method 
        return a + b + c

obj = MathOps()
# print(obj.add(10,20))
print(obj.add(10,20,30))


# Handling Overloading Python way 
class Maths:
    def add(self,a=0,b=0,c=0): # overwrites the above method 
        return a + b + c
    
new_obj = Maths()
print(new_obj.add(10))
print(new_obj.add(10,20))
print(new_obj.add(10,20,30))    