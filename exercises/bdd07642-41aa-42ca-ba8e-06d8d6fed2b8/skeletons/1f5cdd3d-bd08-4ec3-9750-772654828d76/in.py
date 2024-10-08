class MagicalCreature:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display_info(self):
        print('Name:', self.name)
        print('Type:', self.type)

creature = MagicalCreature('Hippogriff', 'Beast')
creature.display_info()