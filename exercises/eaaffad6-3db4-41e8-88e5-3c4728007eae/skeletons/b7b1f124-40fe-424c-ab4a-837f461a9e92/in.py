def mix_potion(ingredients):
    effects = []
    for ingredient in ingredients:
        # Determine effect of ingredient
        effects.append(ingredient_effect(ingredient))
    return effects