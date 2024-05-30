# Hierarchical Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")
        
class Fish:
    def swim(self):
        print("Fish swims")

# Hybrid Inheritance
class Amphibian(Animal, Fish):
    pass

cat = Cat()
cat.speak()
cat.meow()