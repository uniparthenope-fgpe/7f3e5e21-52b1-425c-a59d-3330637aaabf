class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Jedi(Character):
    def attack(self, target):
        target.health -= 10
        print(f'{self.name} attacks {target.name} for 10 damage!')

class Sith(Character):
    def attack(self, target):
        target.health -= 15
        print(f'{self.name} attacks {target.name} for 15 damage!')

luke = Jedi('Luke Skywalker', 100)
darth = Sith('Darth Vader', 100)
luke.attack(darth)
print(darth.health)