
# 6 Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self , meassage):
        self.meassage = meassage
        print(f"Logger Created: {self.meassage}")

    def __del__(self):
        print(f"Logger Destroyed: {self.meassage}")


logger1:Logger = Logger("1st Logger") 
Logger2:Logger = Logger("2nd Logger")
logger1.meassage = "3st Logger"
del logger1
del Logger2
