#1 Print Hello World
print("Hello, Ruben (World)")

#2a Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function
name = "Ruben"
print("Hello,", name)

#2b Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function (#2b)
print("Hello, " + name)

#3a Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function (#3a)
num = 25
print("Hello ", num)

#3b Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)
#NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
print("Hello " + str(num))

#4a Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method (#4a)
fav_food_one = "Lasagna"
fav_food_two = "Pasta"
print("I love to eat {} and {}.".format(fav_food_one, fav_food_two))

#4b Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings (#4b)
print(f"I love to eat {fav_food_one} and {fav_food_two}.")