class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.balance = balance
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
    
# Creating an object
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
# account.balance  = 2000
print(account.get_balance())