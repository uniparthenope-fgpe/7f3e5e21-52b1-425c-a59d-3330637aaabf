class Wizard:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.spells = ['Stupefy', 'Expelliarmus']

class Basilisk:
    def __init__(self):
        self.health = 150

# Simulate duel
wizard = Wizard('Harry')
basilisk = Basilisk()

while wizard.health > 0 and basilisk.health > 0:
    # Wizard attacks
    basilisk.health -= 20
    # Basilisk attacks
    wizard.health -= 15

# Determine winner
if wizard.health > 0:
    print('Wizard wins!')
else:
    print('Basilisk wins!')