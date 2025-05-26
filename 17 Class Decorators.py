# Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
def add_greeting(cls):
    def greet(self):
        return "\tHello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def display(self, message):
        print(message)
        print(f"\tName: {self.name}")

person1 = Person("Alice")
person1.display("\n1st Person Details :")
print(person1.greet())

person2 = Person("Bob")
person2.display("\n2nd Person Details :")
print(person2.greet())
