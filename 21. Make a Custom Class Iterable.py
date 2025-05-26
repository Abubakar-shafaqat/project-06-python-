
# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            current_value = self.current
            self.current -= 1
            return current_value

    def display(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        print(f"\tCountdown Start: {self.start}")
        
Countdown1:Countdown = Countdown(5)
Countdown1.display("\n1st Countdown Details :")
for number in Countdown1:
    print(f"\tCountdown Number: {number}")
    
