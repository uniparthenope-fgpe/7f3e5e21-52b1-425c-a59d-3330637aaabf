class Potion:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def mix(self):
        return f'Mixing {self.name} with {', '.join(self.ingredients)}'
    def check_potency(self):
        return len(self.ingredients) * 10  # Example potency calculation