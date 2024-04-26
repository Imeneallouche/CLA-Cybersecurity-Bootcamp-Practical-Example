class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
dog = Dog("Buddy")
print(dog.name, "says", dog.speak())

cat = Cat("Whiskers")
print(cat.name, "says", cat.speak())
