# Types Of Inheritance 

# Single Level Inheritance : -> One Parent -> One Child 

class Father:
    def house(self):
        print("Has House")
        
class Son(Father):
    def car(self):
        print("Has Car")
        
son_obj = Son()    
son_obj.car()
son_obj.house()

# Multi Level Inheritance : Parent -> Child -> GrandChild 
class GrandParent:
    def land(self):
        print("Has Agriculture Land")
        
class Father(GrandParent):
    def house(self):
        print("Has House")
        
class Son(Father):
    def car(self):
        print("Has Car")
son_obj = Son()    
son_obj.car()
son_obj.house()
son_obj.land()

# Multiple Inheritance : One Child -> Multiple Parents 
class GrandParent:
    def land(self):
        print("Has Agriculture Land")
        
class Father(GrandParent):
    def house(self):
        print("Has House")

class Mother():
    def gold(self):
        print("Has Gold")
        
class Son(Father,Mother): # applying multiple inheritance
    def car(self):
        print("Has Car")
son_obj = Son()    
son_obj.car()
son_obj.house()
son_obj.land()
son_obj.gold()

# Hierarchial Inheritance : One Parent -> Multiple Child
class GrandParent:
    def land(self):
        print("Has Agriculture Land")
        
class Father(GrandParent):
    def house(self):
        print("Has House")

class Mother():
    def gold(self):
        print("Has Gold")
        
class Daughter(Father):
    def business(self):
        print("Has Business")
        
class Son(Father): 
    def car(self):
        print("Has Car")

son_obj = Son()    
son_obj.car()
son_obj.house()
son_obj.land()

daughter_obj = Daughter()
daughter_obj.business()
daughter_obj.house()
daughter_obj.land()

# Hybrid Inheritance : Combination or two or more types 

class A:
    def feat1(self):
        print("Feature 1")

class B(A):
    def feat2(self):
        print("Feature 2") 

class C(A):
    def feat3(self):
        print("Feature 3")

class D(B,C):
    def feat4(self):
        print("Feature 4")
        
obj = D()
obj.feat1()
obj.feat2()
obj.feat3()
obj.feat4()