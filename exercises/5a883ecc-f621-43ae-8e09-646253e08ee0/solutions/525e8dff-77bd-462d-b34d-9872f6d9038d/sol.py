class Jedi:
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def attack(self, opponent):
        opponent.health -= 10

class Sith:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        opponent.health -= 10

jedi = Jedi('Luke')
sith = Sith('Vader')

while jedi.health > 0 and sith.health > 0:
    jedi.attack(sith)
    sith.attack(jedi)
print('Battle Over!')