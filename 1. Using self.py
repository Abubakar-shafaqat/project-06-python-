# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self , name,Class, marks , subjects ):
        self.name = name
        self.marks = marks
        self.Class = Class
        self.subjects = subjects
        
    def display(self,meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\tName: {self.name}, Class: {self.Class}, Marks: {self.marks} , Subjects: {self.subjects}")

students1:Student = Student("John",5, 85 , ["Math", "Science"])
students1.display("\n1st Student Details :")
students2:Student = Student("Alice",6, 90 , ["English", "History"])
students2.display("\n2nd Student Details :")
student3:Student = Student("Bob",7, 78 , ["Geography", "Art"])
student3.display("\n3rd Student Details :")
