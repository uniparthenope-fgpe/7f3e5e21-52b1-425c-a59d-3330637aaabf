class Starship:
    def __init__(self, distance, fuel):
        self.distance = distance
        self.fuel = fuel
    
    def fuel_efficiency(self):
        return self.distance / self.fuel if self.fuel > 0 else 0