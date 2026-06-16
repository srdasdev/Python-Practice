"""Definition: Hide internal details and expose only what's necessary.

Real-World Analogy: A car's engine — you don't need to know how it works, just use the steering wheel and pedals."""

class BankAccount:
    def __init__(self, account_number, balance):
        print("Initializing BankAccount...")
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")


    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

account = BankAccount("123456789", 1000)
account.deposit(500)  # Depositing money to the account
print(f"Account Number: {account.get_account_number()}")  # Accessing private attribute
print(f"Initial Balance: {account.get_balance()}")  # Accessing private attribute

# account.__balance = 999  ❌ Can't directly access private attribute, will raise an AttributeError