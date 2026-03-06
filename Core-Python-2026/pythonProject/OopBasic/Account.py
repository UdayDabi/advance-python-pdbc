class Account:
    def __init__(self):
        self.__number = None
        self.__accountType = None
        self.__balance = 0.0

    # Getter and Setter for number
    def get_number(self):
        return self.__number

    def set_number(self, number):
        print("Setting account number to:", number)
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


a = Account()
a.set_number("12345")
a.set_account_type("Saving")
a.set_balance(1000)
print("Account Number:", a.get_number())
print("Account Type:", a.get_account_type())
print("Balance:", a.get_balance())