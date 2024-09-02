"""
You are working for MNC Bank Ltd. There is a master file (dataCustomerAccountBalanceFIle.csv) containing 
customer id and current balance in their accounts. We need to calculate basic interest at a rate of 4% per 
annum. However, no interest is calculated if the current balance is less than 100.00. These cases must be 
reported.
Write a Python program:
• Calculate interest for each account. Extend the above BankAccount class that will have a method 
calculateInterest() to calculate interest and return the amount. If the current balance is less than 
100.00, then, interest is not calculated.
• Where interest is calculated, the customer id and the interest amount should be written to an output 
file named InterestAmount.csv
• Where interest is not calculated, the customer id and the current balance amount should be written 
to a DefaultCustomerFile.csv
"""
import csv

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

    def calculateInterest(self):
        i = (self.amount * 12 * 4) / 100
        return i
    
cust = []
def_cust = []
with open('data/dataCustomerAccountBalanceFIle.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if int(row[1]) >= 100:
            object = BankAccount()
            object.deposit(int(row[1]))
            intr = object.calculateInterest()
            # print(int(row[0]), intr)
            cust.append([int(row[0]), intr])
        else:
            def_cust.append([int(row[0]), row[1]])

with open('data/InterestAmount.csv', 'a', newline='') as f:
    f.seek(0,0)
    writer = csv.writer(f)
    writer.writerows(cust)

with open('data/DefaultCustomerFile.csv', 'a', newline='') as f:
    f.seek(0,0)
    writer = csv.writer(f)
    writer.writerows(def_cust)

print(cust)