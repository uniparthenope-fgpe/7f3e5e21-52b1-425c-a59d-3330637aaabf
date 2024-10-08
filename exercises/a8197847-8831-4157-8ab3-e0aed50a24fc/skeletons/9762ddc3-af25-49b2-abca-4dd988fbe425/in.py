class Spell:
    def __init__(self, name):
        self.name = name
    
    def cast(self):
        if self.name == 'Expelliarmus':
            return 'Disarms opponent'
        ________

spell = Spell('Expelliarmus')
print(spell.cast())