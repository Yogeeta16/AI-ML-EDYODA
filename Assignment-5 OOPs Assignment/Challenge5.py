class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance for withdrawal.")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print("Invalid deposit amount.")

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

# Testing the code


demo1 = SavingsAccount("Ashish", 2000, 5)

# Perform operations

print("initially ")
print("Current Balance:", demo1.getBalance())
print("Interest Amount:", demo1.interestAmount())

print("----------------------------------------------------------------------------------------------")

demo1.deposit(500)
print("after deposit ")
print("Current Balance:", demo1.getBalance())
print("Interest Amount:", demo1.interestAmount())

print("----------------------------------------------------------------------------------------------")

demo1.withdrawal(300)
print("after withdrawal ")
print("Current Balance:", demo1.getBalance())
print("Interest Amount:", demo1.interestAmount())

print("----------------------------------------------------------------------------------------------")
