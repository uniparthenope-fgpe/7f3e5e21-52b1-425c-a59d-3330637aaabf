class Spell:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class DefenseSpell(Spell):
    def cast(self):
        if self.power < 0:
            raise ValueError('Power cannot be negative')
        return f'Casting {self.name} with power {self.power}'