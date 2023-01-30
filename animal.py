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

def animal_speak(animals):
    for animal in animals:
        print(animal.name, 'says', animal.speak())

animals = Dog("Fido"), Cat("Whiskers"), Dog("Buddy")
print(animals)
animal_speak(animals)
