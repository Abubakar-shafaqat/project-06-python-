
# Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"\tEngine with {self.horsepower} HP started.")
        
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\t{self.brand} car is starting.")
        self.engine.start()


engine1:Engine = Engine(150)
car1:Car = Car("Toyota" , engine1)
car1.start("\n1st Car Details :")
engine2:Engine = Engine(200)
car2:Car = Car("Honda" , engine2)
car2.start("\n2nd Car Details :")
engine3:Engine = Engine(250)
car3:Car = Car("BMW" , engine3)
car3.start("\n3rd Car Details :")
