class BankAccount:
    def __init__(self, name, int_rate, account):
        self.name = name
        self.int_rate = int_rate
        self.account = account

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdraw(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(
            f"Name: {self.name}\nInterst Rate: {self.int_rate}\nBalance: {self.account}")

    def yield_interest(self):
        self.account += self.int_rate * self.account
        return self

class User:
    def __init__(self, first_name, last_name, email, age, account):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"Full Name: {self.first_name} {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nRewards: {self.is_rewards_member}\nGold Points: {self.gold_card_points}")
        return self
    
    #  Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    
    # have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self
    
ruben = BankAccount("Ruben", int("4"), int("1000"))
ocasio = BankAccount("David", int("4"), int("0"))

ruben.make_deposit(int(500)).make_deposit(500).make_withdraw(500).make_withdraw(500).display_user_balance()
ocasio.make_deposit(int(500)).make_deposit(500).make_withdraw(500).make_withdraw(500).display_user_balance()
