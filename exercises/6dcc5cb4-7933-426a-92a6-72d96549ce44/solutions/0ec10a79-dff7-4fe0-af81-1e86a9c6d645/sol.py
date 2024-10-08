potions = []

def add_potion(name, ingredients):
    potions.append({'name': name, 'ingredients': ingredients})


def view_potions():
    for potion in potions:
        print(f"Potion: {potion['name']}, Ingredients: {', '.join(potion['ingredients'])}")