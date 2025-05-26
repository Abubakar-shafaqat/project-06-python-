#  Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self , name , breed):
        self.name = name
        self.breed = breed

    def bark(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"{self.name} the {self.breed} says Woof!")

Dog1:Dog = Dog("Buddy" , "Golden Retriever")
Dog1.bark("\n1st Dog Details :")    
Dog2:Dog = Dog("Max" , "Bulldog")
Dog2.bark("\n2nd Dog Details :")
Dog3:Dog = Dog("Bella" , "Beagle")
Dog3.bark("\n3rd Dog Details :")

