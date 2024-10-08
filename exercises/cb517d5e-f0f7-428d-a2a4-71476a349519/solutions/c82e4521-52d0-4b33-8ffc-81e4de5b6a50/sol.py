potions = []

def add_potion(name):
    potions.append(name)

def list_potions():
    return potions

def search_potion(name):
    return name in potions