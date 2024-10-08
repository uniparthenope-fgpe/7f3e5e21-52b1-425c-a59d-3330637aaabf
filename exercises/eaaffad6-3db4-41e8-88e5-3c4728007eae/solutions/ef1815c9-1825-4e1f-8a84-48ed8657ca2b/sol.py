def mix_potion(ingredients):
    effects = []
    for ingredient in ingredients:
        effects.append(ingredient_effect(ingredient))
    return ' and '.join(effects)

def ingredient_effect(ingredient):
    effects_dict = {'Mandrake': 'Healing', 'Dragon Blood': 'Strength', 'Powdered Unicorn Horn': 'Wisdom'}
    return effects_dict.get(ingredient, 'Unknown Effect')