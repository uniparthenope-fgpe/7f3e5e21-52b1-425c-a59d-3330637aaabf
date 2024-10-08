class MagicalCreature:
    def __init__(self, name, creature_type):
        self.name = name
        self.creature_type = creature_type
    def describe(self):
        return f'{self.name} is a {self.creature_type}.'