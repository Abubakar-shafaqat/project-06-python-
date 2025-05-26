# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Habib Bank Limited"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def __init__(self , account_number):
        self.account_number = account_number
        

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"Account Number: {self.account_number}, Bank Name: {Bank.bank_name}")
        
acount1:Bank = Bank("123456789")
acount1.display("\n1st Account Details :")
acount2:Bank = Bank("987654321")
acount2.display("\n2nd Account Details :")
Bank.change_bank_name("Bank Alfalah")
acount3:Bank = Bank("456789123")
acount3.display("\n3rd Account Details :")
acount4:Bank = Bank("321654987")    
acount4.display("\n4th Account Details :")
