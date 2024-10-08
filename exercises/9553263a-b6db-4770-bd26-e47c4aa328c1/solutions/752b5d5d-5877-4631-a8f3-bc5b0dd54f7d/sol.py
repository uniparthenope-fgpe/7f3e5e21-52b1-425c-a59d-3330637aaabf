inventory = {}
def add_droid(name, type):
    inventory[name] = type

def display_inventory():
    for name, type in inventory.items():
        print(f'{name}: {type}')

# Example usage
add_droid('R2-D2', 'Astromech')
display_inventory()