"""
Classes and Objects:
- Class is a blueprint.
- Object is an instance of a class. Means an object is created using the
template, that is, the class.

- self: self indicates the current object. Every method needs self as it's
first parameter.
- __init__ is called automatically when you instantiate a class.
- Attributes: properties / data that the object holds (name, breed)
- Methods: functions that the object can perform (bark)
- You can create many objects using a class. Example below.

"""


# class & object example:
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"The dog, {self.name}, is barking: woof woof!"


# define an object:
charlie = Dog("Charlie", "Labrador")
goofy = Dog("Goofy", "Bulldfdog")

print(charlie.bark())
print(goofy.bark())


# check:
print(charlie == goofy)
