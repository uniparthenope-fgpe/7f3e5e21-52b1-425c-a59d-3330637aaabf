class Wizard:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def cast_spell(self, other):
        damage = 10
        other.health -= damage
        print(f'{self.name} casts a spell on {other.name} for {damage} damage!')

# Simulate the duel
wizard1 = Wizard('Harry')
wizard2 = Wizard('Draco')
while wizard1.health > 0 and wizard2.health > 0:
    wizard1.cast_spell(wizard2)
    if wizard2.health <= 0:
        print(f'{wizard2.name} has been defeated!')
        break
    wizard2.cast_spell(wizard1)
    if wizard1.health <= 0:
        print(f'{wizard1.name} has been defeated!')
        break