class Spell:
    def __init__(self, name, incantation, effect):
        self.name = name
        self.incantation = incantation
        self.effect = effect

    def display_spell(self):
        return f'Spell: {self.name}, Incantation: {self.incantation}, Effect: {self.effect}'