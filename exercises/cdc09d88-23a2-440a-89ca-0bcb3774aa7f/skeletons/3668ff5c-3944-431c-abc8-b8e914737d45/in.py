class Wizard:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def cast_spell(self, spell):
        if spell == 'Expelliarmus':
            self.health -= 10
        # Missing else condition for other spells

harry = Wizard('Harry', 100)

# Simulate duel
harry.cast_spell('Expelliarmus')
print(harry.health)  # Should print 90