class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} the Dog says Woof Woof!")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} the Cat says Meow Meow!")
animal = Animal("Cow", "Moo")
dog = Dog("Tommy", "Woof")
cat = Cat("Kitty", "Meow")
animal.speak()
dog.speak()
cat.speak()