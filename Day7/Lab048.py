# Multiple Inheritance

class Bird:
    def fly(self):
        print("Bird flies")
        
class Fish:
    def swim(self):
        print("Fish swims")
        
        
class FlyingFish(Bird, Fish):
    def print(self):
        print("Hello")


flying_fish = FlyingFish()
flying_fish.fly()
flying_fish.swim()