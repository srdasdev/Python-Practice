"""Definition: Hide internal details and expose only what's necessary.

Real-World Analogy: A car's engine — you don't need to know how it works, just use the steering wheel and pedals."""

# class BankAccount:
#     def __init__(self, account_number, balance):
#         print("Initializing BankAccount...")
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: {amount}. New Balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")


#     def get_balance(self):
#         return self.__balance

#     def get_account_number(self):
#         return self.__account_number

# account = BankAccount("123456789", 1000)
# account.deposit(500)  # Depositing money to the account
# print(f"Account Number: {account.get_account_number()}")  # Accessing private attribute
# print(f"Initial Balance: {account.get_balance()}")  # Accessing private attribute

# account.__balance = 999  ❌ Can't directly access private attribute, will raise an AttributeError



# Implement the same using property decorator to access the private attributes.

class BankAccount:
    def __init__(self,account_number, balance):
        print("Initializing BankAccount...")
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount<0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount
    @balance.deleter
    def balance(self):
        print(f"Closing account — clearing balance of {self.__balance}")
        del self.__balance
    
    @property
    def account_number(self):
        return self.__account_number
    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

account = BankAccount("123456789", 1000)
account.deposit(500)  # Depositing money to the account
print(f"Account Number: {account.account_number}")  # Accessing private attribute using property
account.balance = 2000  # Setting balance using setter

# del account.balance  # Deleting balance using deleter

print(f"Updated Balance: {account.balance}")  # Accessing private attribute using property

# account.balance = -500  # This will raise a ValueError because balance cannot be negative.