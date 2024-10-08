class Wizard:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def cast_spell(self, spell):
        if spell == 'Expelliarmus':
            self.health -= 10
        elif spell == 'Stupefy':
            self.health -= 15
        elif spell == 'Avada Kedavra':
            self.health = 0

harry = Wizard('Harry', 100)

# Simulate duel
harry.cast_spell('Expelliarmus')
print(harry.health)  # Should print 90