class Spell:
    def __init__(self, name):
        self.name = name
    
    def cast(self):
        if self.name == 'Expelliarmus':
            return 'Disarms opponent'
        elif self.name == 'Lumos':
            return 'Creates light'
        elif self.name == 'Aguamenti':
            return 'Produces water'
        else:
            return 'Unknown spell'

spell = Spell('Expelliarmus')
print(spell.cast())