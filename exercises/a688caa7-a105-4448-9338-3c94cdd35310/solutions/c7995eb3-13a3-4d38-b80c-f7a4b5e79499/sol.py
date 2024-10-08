class Starship:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_speed(self):
        return self.speed

class Fleet:
    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def total_speed(self):
        return sum(ship.get_speed() for ship in self.ships)

# Create instances of Starship
ship1 = Starship('X-Wing', 100)
ship2 = Starship('TIE Fighter', 120)

# Create Fleet and add ships
fleet = Fleet()
fleet.add_ship(ship1)
fleet.add_ship(ship2)

# Calculate total speed
print('Total fleet speed:', fleet.total_speed())