from classes.Ninja import Ninja
from classes.Pet import Pet
# from classes.Dog import Dog

dog = Pet("Petey", "Dog", ["Sit", "fetch", "Roll"])
ruben = Ninja("Ruben", "Ocasio", "Biscuits", "Dog food", dog)

dog.sleep().eat().play().noise()
ruben.walk().feed().bathe().info()