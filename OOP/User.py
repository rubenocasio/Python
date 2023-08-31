# Define a new class named User
class User:

    # Constructor method for the User class
    #The __init__ method in Python is a special method called a "dunder" method
    # #(short for "double underscore"). It's also commonly known as the
    # #initializer or constructor method for a class. This method is
    # #automatically called when an object (an instance of the class) is created.
    def __init__(self, first_name, last_name, email, age):
        # Assign the provided first name to the instance variable 'first_name'
        self.first_name = first_name
        # Assign the provided last name to the instance variable 'last_name'
        self.last_name = last_name
        # Assign the provided email to the instance variable 'email'
        self.email = email
        # Assign the provided age to the instance variable 'age'
        self.age = age
        # Initialize the 'is_rewards_member' attribute with a default value of False
        self.is_rewards_member = False
        # Initialize the 'gold_card_points' attribute with a default value of 0
        self.gold_card_points = 0

    # Method to display user information
    def display_info(self):
        # Print the full name, email, age, rewards membership status, and gold points of the user
        print(f"Full Name: {self.first_name} {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nRewards: {self.is_rewards_member}\nGold Points: {self.gold_card_points}")
        # Return the current instance to allow method chaining
        return self

    # Method to enroll the user as a rewards member
    def enroll(self):
        # Update the 'is_rewards_member' attribute to True
        self.is_rewards_member = True
        # Assign 200 points to the 'gold_card_points' attribute for enrolling
        self.gold_card_points = 200
        # Return the current instance to allow method chaining
        return self

    # Method to allow the user to spend their gold card points
    def spend_points(self, amount):
        # Subtract the specified 'amount' from the 'gold_card_points' attribute
        self.gold_card_points -= amount
        # Return the current instance to allow method chaining
        return self

# Create a new User object with the specified details
ruben = User("Ruben", "Ocasio", "ruben@rubenocasio.com", 21)
# Call the 'display_info' method to print Ruben's details
ruben.display_info()
# Call the 'enroll' method to enroll Ruben as a rewards member and give him 200 points
ruben.enroll()
# Print a separator line
print("----------------------------")
# Again, call the 'display_info' method to print updated Ruben's details
ruben.display_info()
# Print another separator line
print("----------------------------")
# Call the 'spend_points' method to spend 50 of Ruben's gold card points
ruben.spend_points(50)
# Once more, call the 'display_info' method to print Ruben's updated details after spending points
ruben.display_info()


