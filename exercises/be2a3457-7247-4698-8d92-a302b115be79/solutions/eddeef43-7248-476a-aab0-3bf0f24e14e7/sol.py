class Wizard:
    def __init__(self, name):
        self.name = name
    def cast_spell(self, spell):
        print(f'{self.name} casts {spell}!')