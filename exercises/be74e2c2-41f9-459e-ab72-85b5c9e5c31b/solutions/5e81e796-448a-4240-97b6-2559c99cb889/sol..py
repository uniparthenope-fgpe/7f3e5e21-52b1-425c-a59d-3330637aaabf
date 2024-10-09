class Student:
    def __init__(self, name):
        self.name = name
        self.spells_learned = []

    def learn_spell(self, spell):
        self.spells_learned.append(spell.name)

class Spell:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

# Example usage
harry = Student('Harry Potter')
expelliarmus = Spell('Expelliarmus', 2)
harry.learn_spell(expelliarmus)
print(harry.spells_learned)