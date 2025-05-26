

# Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
class AgeValidator:
    def __init__(self, age):
        self.age = age

    def check_age(self):
        if self.age < 18:
            raise InvalidAgeError("Age must be 18 or older.")
        else:
            print(f"Age {self.age} is valid.")

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\tAge: {self.age}")
ageValidator1:AgeValidator = AgeValidator(2)
ageValidator1.display("\n1st Age Validator Details :")
try:
    ageValidator1.check_age()
except InvalidAgeError as e:
    print(f"Error: {e.message}")
    
    
ageValidator2:AgeValidator = AgeValidator(20)
ageValidator2.display("\n2nd  Age Validator Details :")
try:
    ageValidator1.check_age()
except InvalidAgeError as e:
    print(f"Error: {e.message}")
