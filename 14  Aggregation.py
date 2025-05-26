#  Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class Department:
    def __init__(self, name):
        self.name = name

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\t\tDepartment: {self.name}")


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\tEmployee: {self.name}")
        self.department.display("\tDepartment Details :")


department1:Department = Department("HR")
employee1:Employee = Employee("Alice" , department1)
employee1.display("\n1st Employee Details :")   

department2:Department = Department("IT")
employee2:Employee = Employee("Bob" , department2)
employee2.display("\n2nd Employee Details :")

department3:Department = Department("Finance")
employee3:Employee = Employee("Charlie" , department3)
employee3.display("\n3rd Employee Details :")

