class Account:

    def __init__(self):
        self.__number = None
        self.__accountType = None
        self.__balance = 0.0

    # Getter and Setter for number
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    # Getter and Setter for account type
    def get_account_type(self):
        return self.__accountType

    def set_account_type(self, account_type):
        self.__accountType = account_type

    # Getter and Setter for balance
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    # Deposit method
    def deposit(self, amt):
        self.__balance = self.__balance + amt
        print("Total balance after deposit:", self.__balance)

    # Withdrawal method
    def withdrawal(self, amt):
        if amt < self.__balance:
            self.__balance = self.__balance - amt
            print("Total balance after withdrawal:", self.__balance)
        else:
            print("Insufficient fund transfer")


# Example usage
acc = Account()
acc.set_number("12345")
acc.set_account_type("Saving")
acc.set_balance(1000)
print("Account Number:", acc.get_number())
print("Account Type:", acc.get_account_type())
print("Balance:", acc.get_balance())

print("\nPerforming transactions:")
acc.deposit(500)
acc.withdrawal(2000)
