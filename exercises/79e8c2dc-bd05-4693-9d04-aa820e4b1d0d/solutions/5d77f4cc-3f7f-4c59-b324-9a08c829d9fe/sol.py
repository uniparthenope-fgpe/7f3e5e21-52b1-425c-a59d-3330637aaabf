potions = {}

def add_potion(name, ingredients):
    potions[name] = ingredients

# Add potion example
add_potion('Polyjuice Potion', [' lacewing flies', ' leeches', ' powdered bicorn horn'])

# Search for a potion

def search_potion(name):
    return potions.get(name, 'Potion not found')