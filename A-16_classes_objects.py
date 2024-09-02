"""
Create a Python class “BankAccount” with withdraw() and deposit() methods. Then create 2 users “sam” 
and “rio”. Users will deposit and withdraw some amount and program should display their current 
balance.
Input Output
sam.deposit(100) 100
rio.deopsit(200) 200
sam.withdraw(20) 80
rio.withdraw(30) 170
"""

class BankAccount:
    def __init__(self):
        self.amount = 0
        
    def withdraw(self, amt):
        self.amount = self.amount-amt
        print(f"{amt} withdrawn")
        print(f"{self.amount} is the remaining balance")

    def deposit(self, amt):
        self.amount = self.amount+amt
        print(f"{amt} Deposited")
        print(f"{self.amount} is the remaining balance")

sam = BankAccount()
print("---Sam transactions--")
sam.deposit(100)

rio = BankAccount()
print("---Rio transactions--")
rio.deposit(200)

print("---Sam transactions--")
sam.withdraw(20) 
print("---Rio transactions--")
rio.withdraw(30) 