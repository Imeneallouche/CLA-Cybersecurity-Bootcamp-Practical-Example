class BankAccount:

    # the constructor method 
    # always there, automatically called, initializes the class attributes
    def __init__(self, x):
        # self.{attribute)}
        # self._(attribute)
        # self.__(attribute)
        self.__balance = x
    

    # method 1 of the class, an action that an object of this class could do
    # deposit money: increments the balance with the amount deposited 
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "completed.")

    # method 2
    # withdraw: decrements the balance with the amount withdrawed
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "completed.")
        else:
            print("Insufficient funds.")

    # called getter, preferably each private attribute should have a getter
    # it retuns the value of an attribute of an object
    # why? because the object attribute values are encapsulated (private), only the class could see it from inside in a direct way
    def get_balance(self):
        return self.balance




# MAIN PROGRAM 
# Create a bank account object
account = BankAccount()

print(account.get_balance())

#account.deposit(100)
