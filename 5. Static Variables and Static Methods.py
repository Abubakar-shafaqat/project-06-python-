
# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    def __init__(self , meassage ,a , b):
        self.meassage = meassage
        print(self.meassage)
        self.a = a
        self.b = b
        print(f"\tSum of {self.a} and {self.b} is : {MathUtils.add(self.a, self.b)}")

sum1:MathUtils = MathUtils("\n1st Sum Calculation : ", 5, 10)
sum2:MathUtils = MathUtils("\n2nd Sum Calculation : ", 15, 20)
sum3:MathUtils = MathUtils("\n3rd Sum Calculation : ", 25, 30)
