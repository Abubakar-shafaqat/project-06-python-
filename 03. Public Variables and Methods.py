# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self , brand ,modle):
        self.brand = brand
        self.modle = modle

    def start(self):
        print(f"{self.brand} car is starting.")


car1:Car = Car("Toyota" , "Corolla")
car1.start()    
print(f"Car Brand: {car1.brand} , Car Modle: {car1.modle}")
car2:Car = Car("Honda" , "Civic") 
car2.start()
print(f"Car Brand: {car2.brand} , Car Modle: {car2.modle}")
