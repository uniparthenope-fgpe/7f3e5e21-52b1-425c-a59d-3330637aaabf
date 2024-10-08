class MagicalCreature:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Encyclopedia:
    def __init__(self):
        self.creatures = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def remove_creature(self, creature_name):
        self.creatures = [c for c in self.creatures if c.name != creature_name]

    def search_creature(self, creature_name):
        for creature in self.creatures:
            if creature.name == creature_name:
                return creature
        return None