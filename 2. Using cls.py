# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0

    def __init__(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created : {cls.count}")

obj1:Counter = Counter("1st Object Created")
obj2:Counter = Counter("2nd Object Created")
obj3:Counter = Counter("3rd Object Created")
obj4:Counter = Counter("4th Object Created")
Counter.display_count()
