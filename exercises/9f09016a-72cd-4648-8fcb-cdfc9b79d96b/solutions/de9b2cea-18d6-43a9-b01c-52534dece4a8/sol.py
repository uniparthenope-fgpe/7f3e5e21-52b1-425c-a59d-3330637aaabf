class MagicalCreature:
    def __init__(self, name):
        self.name = name
        self.registry = []
    
    def add_creature(self, creature):
        self.registry.append(creature)
    
    def find_creature(self, name):
        for creature in self.registry:
            if creature.name == name:
                return creature
        return None