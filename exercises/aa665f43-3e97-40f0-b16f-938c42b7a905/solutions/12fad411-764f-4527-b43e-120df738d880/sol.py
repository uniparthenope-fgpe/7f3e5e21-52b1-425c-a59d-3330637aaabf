class Wizard:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.spells = ['Stupefy', 'Expelliarmus']

    def cast_spell(self, spell, target):
        if spell in self.spells:
            target.health -= 20

class Basilisk:
    def __init__(self):
        self.health = 150

    def attack(self, target):
        target.health -= 15

# Simulate duel
wizard = Wizard('Harry')
basilisk = Basilisk()

while wizard.health > 0 and basilisk.health > 0:
    wizard.cast_spell('Stupefy', basilisk)
    basilisk.attack(wizard)

# Determine winner
if wizard.health > 0:
    print('Wizard wins!')
else:
    print('Basilisk wins!')