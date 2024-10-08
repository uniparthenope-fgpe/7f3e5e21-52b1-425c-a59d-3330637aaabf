class Character:
    def __init__(self, name):
        self.name = name

class Jedi(Character):
    def use_force(self):
        return 'Using the Force!'

class Sith(Character):
    def use_dark_side(self):
        return 'Embracing the Dark Side!'

jedi = Jedi('Luke')
sith = Sith('Vader')
# Simulate battle
print(jedi.use_force())
print(sith.use_dark_side())