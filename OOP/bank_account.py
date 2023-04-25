class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

        # increases the account balance by the given amount
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self
    
    def display_account_info(self):
        # your code here
        print(f"Interst Rate:{self.int_rate} Balance:{self.balance}")
        return self
    
    def yield_interest(self):
        # your code here
        self.balance += self.int_rate * self.balance
        return self
    

ruben = BankAccount(float(.04), float(1000))
ocasio = BankAccount(float(.05), float(1000))

ruben.deposit(500).display_account_info().withdraw(200).display_account_info().yield_interest().display_account_info()
ocasio.deposit(500).display_account_info().withdraw(200).display_account_info().yield_interest().display_account_info()