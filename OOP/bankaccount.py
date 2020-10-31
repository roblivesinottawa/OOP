class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


acct = BankAccount('Rob')
print(acct.owner)
print(acct.balance)
print(acct.deposit(100))
print(acct.withdraw(30))
print(acct.balance)
