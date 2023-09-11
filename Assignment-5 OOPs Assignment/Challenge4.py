
# method one 
class Account:

    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate


account1 = Account("Ashish", 5000)
print("Account Title:", account1.title)
print("Account Balance:", account1.balance)

savings_account1 = SavingsAccount("Ashish", 5000, 5)
print("Savings Account Title:", savings_account1.title)
print("Savings Account Balance:", savings_account1.balance)
print("Savings Account Interest Rate:", savings_account1.interestRate)
# ------------------------------------------------------------------------------------------------------
print("----------------------------------------------------------------------------------------------")
# ------------------------------------------------------------------------------------------------------
# second method where details will be taken from user 

class Account:

    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

# user input for account details
title = input("Enter the account title: ")
balance = float(input("Enter the account balance: "))
interestRate = float(input("Enter the interest rate for savings account: "))

#instances with user-input details
account1 = Account(title, balance)
savings_account1 = SavingsAccount(title, balance, interestRate)

# Print the details
print("Account Title:", account1.title)
print("Account Balance:", account1.balance)

print("Savings Account Title:", savings_account1.title)
print("Savings Account Balance:", savings_account1.balance)
print("Savings Account Interest Rate:", savings_account1.interestRate)
