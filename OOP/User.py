class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
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


ruben = User("Ruben", "Ocasio", "ruben@rubenocasio.com", 21)
ruben.display_info()
ruben.enroll()
print("----------------------------")
ruben.display_info()
print("----------------------------")
ruben.spend_points(50)
ruben.display_info()

