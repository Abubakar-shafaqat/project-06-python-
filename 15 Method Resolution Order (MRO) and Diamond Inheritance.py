# Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print("Class A: Base class method called.")
class B(A):
    def show(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print("Class B: Derived class method called.")
class C(A):
    def show(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print("Class C: Derived class method called.")
class D(B , C):
    def show(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print("Class D: Derived class method called.")
        super().show("\tCalling super() to resolve MRO:")
        super(B , self).show("\tCalling super(B, self) to resolve MRO:")
        super(C , self).show("\tCalling super(C, self) to resolve MRO:")
class D1(D):
    def show(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print("Class D1: Derived class method called.")
        super().show("\tCalling super() to resolve MRO:")
        super(B , self).show("\tCalling super(B, self) to resolve MRO:")
        super(C , self).show("\tCalling super(C, self) to resolve MRO:")
class1:A = A()
class1.show("\n1st Class A Details :")
class2:B = B()  
class2.show("\n2nd Class B Details :")
class3:C = C()
class3.show("\n3rd Class C Details :")
class4:D = D()
class4.show("\n4th Class D Details :")
class5:D1 = D1()
class5.show("\n5th Class D1 Details :")
