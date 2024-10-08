class Wizard:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def cast_spell(self, other):
        # Complete this method
        pass

# Simulate the duel
wizard1 = Wizard('Harry')
wizard2 = Wizard('Draco')
while wizard1.health > 0 and wizard2.health > 0:
    # Duel logic here