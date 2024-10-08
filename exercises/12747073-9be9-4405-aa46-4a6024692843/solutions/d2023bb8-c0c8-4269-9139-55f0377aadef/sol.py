ingredients = {
    'Wiggenweld': 'healing',
    'Polyjuice': 'transformation',
    'Felix Felicis': 'luck'
}

selected_ingredients = ['Wiggenweld', 'Felix Felicis']

def mix_potion(selected_ingredients):
    effects = []
    for ingredient in selected_ingredients:
        effects.append(ingredients[ingredient])
    return effects

print(mix_potion(selected_ingredients))