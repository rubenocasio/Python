from Pet import Pet

class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Dog", tricks)

    def noise(self):
        print(f"{self.name} barks!")
