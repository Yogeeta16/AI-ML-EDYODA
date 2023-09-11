class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Cannot divide by zero"
        return self.num2 / self.num1

obj = Calculator(10, 94)
print(obj.add())       # Output: 104
print(obj.subtract())  # Output: 84
print(obj.multiply())  # Output: 940
print(obj.divide())    # Output: 9.4


obj2 = Calculator(10, 35)
print(obj2.add())       # Output: 45
print(obj2.subtract())  # Output: 25
print(obj2.multiply())  # Output: 350
print(obj2.divide())    # Output: 3.5