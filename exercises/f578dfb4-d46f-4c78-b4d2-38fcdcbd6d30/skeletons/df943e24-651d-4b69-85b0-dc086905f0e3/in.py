creatures = {'Hippogriff': 'A magical creature with the front half of an eagle and the back half of a horse.'}

def search_creature(name):
    return creatures.get(name, 'Creature not found')

# Example usage:
search_creature('Hippogriff')