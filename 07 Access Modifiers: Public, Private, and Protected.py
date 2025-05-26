
#  7 Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self , name , salary , ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")
        


employee1:Employee = Employee("Alice" , 50000 , "123-45-6789")
employee1.display("\n1st Employee Details :")
print(f"Accessing Public Variable: {employee1.name}")
print(f"Accessing Protected Variable: {employee1._salary}")
print(f"Accessing Private Variable: {employee1._Employee__ssn}") # Accessing private variable using name mangling

employee2:Employee = Employee("Bob" , 60000 , "987-65-4321")
employee2.display("\n2nd Employee Details :") 
print(f"Accessing Public Variable: {employee2.name}")
print(f"Accessing Protected Variable: {employee2._salary}")
print(f"Accessing Private Variable: {employee2._Employee__ssn}") # Accessing private variable using name mangling
