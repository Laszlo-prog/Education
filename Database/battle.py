class Pokemon:
    def __init__(self, name, fire):
        self.name = name
        self.fire = fire

    def power(self):
        print(f"Use {self.name} Flamethrower {self.fire}")

    def hit(self):
        print("Punch")


class Lizard(Pokemon):
    def power(self):
        print("FlameThrower")

class Turtle(Pokemon):
    def hit(self):
        print("Punch")


p = Pokemon("Charmander", "Attack")
p.power()



#p = Turtle("Squrtle")
