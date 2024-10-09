class Wizard:
    def __init__(self, name):
        self.name = name

    def cast_spell(self):
        return f'{self.name} casts Expelliarmus!'

harry = Wizard('Harry Potter')
print(harry.cast_spell())