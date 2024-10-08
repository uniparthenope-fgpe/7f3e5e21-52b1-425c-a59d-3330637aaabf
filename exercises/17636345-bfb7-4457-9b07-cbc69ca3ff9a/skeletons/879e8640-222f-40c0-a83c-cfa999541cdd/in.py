class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Jedi(Character):
    def attack(self, target):
        pass

class Sith(Character):
    def attack(self, target):
        pass

luke = Jedi('Luke Skywalker', 100)
darth = Sith('Darth Vader', 100)
luke.attack(darth)
print(darth.health)