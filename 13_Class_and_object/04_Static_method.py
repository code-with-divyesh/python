# A static method is a method that belongs to a class,
# but it does not depend on any instance (object) or self.

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# call static methods (no object needed)
print(MathOperations.add(10, 5))
print(MathOperations.multiply(4, 3))


# Abstraction:
# Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation
# Wrapping data and functions into a single unit (object).


class Account:
    # constructor
    def __init__(self, acc_no, balance):
        self.__account_no = acc_no     
        self.__balance = balance        

    # method to credit amount (abstraction)
    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} credited successfully.")
        else:
            print("Invalid amount!")

    # method to debit amount (abstraction)
    def debit(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} debited successfully.")
        else:
            print("Insufficient balance or invalid amount!")

    # method to show balance (abstraction)
    def show_balance(self):
        print(f"Available Balance: ₹{self.__balance}")

    # optional getter for account number (read-only access)
    def get_account_no(self):
        return self.__account_no

# create account object
acc1 = Account(123456789, 5000)

# show account details safely
print("Account No:", acc1.get_account_no())

# credit and debit operations
acc1.credit(2000)
acc1.debit(1500)

# show final balance
acc1.show_balance()
