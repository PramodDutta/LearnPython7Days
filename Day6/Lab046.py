# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Creating objects
dog = Dog("Buddy")


# Accessing methods
print(dog.speak())  # Output: Buddy says Woof!
