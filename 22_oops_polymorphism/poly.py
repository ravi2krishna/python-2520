# method overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def sound(self): # overriding 
        print("Dogs makes a Woff")

class Cat(Animal):
    def sound(self): # overriding 
        print("Cats makes a Meow")
        
class Cow(Animal):
    pass 

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()