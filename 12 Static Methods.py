# Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    def __init__(self , celsius , message):
        self.celsius = celsius
        self.message = message
        print(self.message)
        print(f"\tCelsius: {self.celsius}, Fahrenheit: {Temperature.celsius_to_fahrenheit(self.celsius)}")

Temperature1:Temperature = Temperature(0 , "\n1st Temperature Conversion :")
Temperature2:Temperature = Temperature(100 , "\n2nd Temperature Conversion :")
Temperature3:Temperature = Temperature(37 , "\n3rd Temperature Conversion :")
