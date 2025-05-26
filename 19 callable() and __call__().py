# callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\tMultiplier Factor: {self.factor}")
Multiplier1:Multiplier = Multiplier(5)
Multiplier1.display("\n1st Multiplier Details :")
print(f"\tIs Multiplier1 callable? {callable(Multiplier1)}")
print(f"\tResult of calling Multiplier1 with 10: {Multiplier1(10)}")

Multiplier2:Multiplier = Multiplier(3)
Multiplier2.display("\n2nd Multiplier Details :")
print(f"\tIs Multiplier2 callable? {callable(Multiplier2)}")
print(f"\tResult of calling Multiplier2 with 10: {Multiplier2(10)}")
