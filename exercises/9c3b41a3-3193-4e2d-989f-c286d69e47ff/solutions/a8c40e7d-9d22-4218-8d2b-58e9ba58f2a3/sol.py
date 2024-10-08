class GalacticBattle:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, other_ship):
        other_ship.health -= 10

    def is_alive(self):
        return self.health > 0