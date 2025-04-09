# Hiding internal details and exposing only what's necessary.
#
# Achieved using private variables and getter/setter methods.

class BankAccount:
    def __init__(self):
        self.__balance = 0  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())

