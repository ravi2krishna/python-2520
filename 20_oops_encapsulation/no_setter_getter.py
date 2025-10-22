# No Encapsulation & No Setter - Getter

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
s1 = Student("ravi",95)    
print(s1.name)
print(s1.marks)

s1.marks = -10
print(s1.marks)

s1.marks = 200
print(s1.marks)