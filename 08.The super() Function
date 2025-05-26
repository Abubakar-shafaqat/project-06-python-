
# The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self , name):
        self.name = name

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"Name: {self.name}")


class Teacher(Person):
    def __init__(self , name , subject):
        super().__init__(name)
        self.subject = subject

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"Name: {self.name}, Subject: {self.subject}")



teacher1:Teacher = Teacher("Mr. Smith" , "Mathematics")
teacher1.display("\n1st Teacher Details :")
teacher2:Teacher = Teacher("Ms. Johnson" , "Physics")
teacher2.display("\n2nd Teacher Details :")
teacher3:Teacher = Teacher("Dr. Brown" , "Chemistry")
teacher3.display("\n3rd Teacher Details :")
