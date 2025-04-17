class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        # Base class method, might be overridden by subclasses.
        return "Some generic sound"

    def __str__(self):
        # Gives a human-readable description of the animal.
        return f"{self.name} is {self.age} years old."

    def __eq__(self, other):
        # Equality is defined by both having the same name and age.
        if isinstance(other, Animal):
            return (self.name == other.name) and (self.age == other.age)
        return False

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Testing Exercise 1:
if __name__ == "__main__":
    dog1 = Dog("Buddy", 3)
    cat1 = Cat("Whiskers", 2)
    another_dog = Dog("Buddy", 3)

    print(dog1)          # Uses __str__
    print(cat1)          # Uses __str__
    print("Dog says:", dog1.speak())   # Customized speak method.
    print("Cat says:", cat1.speak())    # Customized speak method.

    # Test the equality using __eq__
    print("dog1 == another_dog:", dog1 == another_dog)  # Expected: True
