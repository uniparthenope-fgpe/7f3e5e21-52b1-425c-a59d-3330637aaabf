class Patronus:
    def __init__(self, animal):
        self.animal = animal
    def cast(self):
        return f'Casting {self.animal} Patronus!'
    def identify(self):
        return f'Your Patronus is a {self.animal}'