class pokemon:
    def __init__(self, name, attack):

        self.name = name
        #self.prototype = prototype
        self.attack = attack
        #self.rezistance = rezistance

    def printname(self):
        print(self.name, self.attack)

class Trainer(pokemon):
    def fetch(self, thing):
        print(self.name, thing)



x = pokemon("Pikachu", "ThunderJolt")
y = Trainer('Ash', 'Ketchump')
x.printname()
y.fetch()




        
