potions = {}

def add_potion(name, ingredients):
    potions[name] = ingredients

def view_potions():
    for potion, ingredients in potions.items():
        print(f'{potion}: {', '.join(ingredients)}')

# Add a potion
add_potion('Polyjuice Potion', ['lacewing flies', 'leeches'])
view_potions()