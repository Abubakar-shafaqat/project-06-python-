

# . Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self ,meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"Area of Rectangle: {self.length * self.width}")
        return self.length * self.width
    

rectangle1:Rectangle = Rectangle(5 , 10)
rectangle1.area("\n1st Rectangle Area Calculation :")
rectangle2:Rectangle = Rectangle(7 , 12)
rectangle2.area("\n2nd Rectangle Area Calculation :")
rectangle3:Rectangle = Rectangle(9 , 15)
rectangle3.area("\n3rd Rectangle Area Calculation :")

