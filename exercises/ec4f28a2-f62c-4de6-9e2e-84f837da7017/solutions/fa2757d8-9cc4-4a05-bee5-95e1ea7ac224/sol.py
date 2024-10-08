class Starship:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def attack(self, other):
        damage = 10
        other.health -= damage
        print(f'{self.name} attacks {other.name} for {damage} damage!')
    def defend(self, damage):
        self.health -= damage // 2
        print(f'{self.name} defends against {damage} damage!')