creatures = {'Unicorn': 'A magical horse', 'Dragon': 'A fire-breathing creature'}

def search_creature(name):
    return creatures.get(name, 'Creature not found')

# Fix the bug here