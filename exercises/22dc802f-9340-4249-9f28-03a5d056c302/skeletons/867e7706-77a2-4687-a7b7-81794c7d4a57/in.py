potions = []

def add_potion(name):
    potions.append(name)

def view_potions():
    return potions

def delete_potion(name):
    potions.remove(name)

# Example usage:
add_potion('Polyjuice Potion')
view_potions()