# Polymorphism
# Polymorphism allows methods to do different things based on the object it is acting upon.
# It can be achieved through method overriding and method overloading.


# Method Overriding:

class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
        
class Cat(Animal):
    def sound(self):
        print("Cat meows")
        
animal_cat = Cat()
animal_dog = Dog()
animal_dog.sound()
animal_cat.sound()