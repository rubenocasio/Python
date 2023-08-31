class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(f"{self.name} makes some noise! My health is: {self.health} and my energy is: {self.energy}")
        return self

