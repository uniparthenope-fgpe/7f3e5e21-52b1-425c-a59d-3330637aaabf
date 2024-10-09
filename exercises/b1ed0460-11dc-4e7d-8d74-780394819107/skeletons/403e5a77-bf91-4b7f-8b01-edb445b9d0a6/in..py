class Potion:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def brew(self):
        return f'Brewing {self.name} with {self.ingredients}'

# Your code here