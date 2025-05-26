#  Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    @price.deleter
    def price(self):
        del self._price

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\tProduct: {self.name}, Price: {self.price}")

product1:Product = Product("Laptop", 1000)
product1.display("\n1st Product Details :")
product1.price = 1200
product1.display("\nUpdated Product Details :")


