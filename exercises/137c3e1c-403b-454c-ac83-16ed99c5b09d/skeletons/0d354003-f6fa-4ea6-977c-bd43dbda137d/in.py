def calculate_ingredients(potions):
    # Fill in the gaps
    ingredients = {
        'eye_of_newt': 2,
        'dragon_blood': 5,
        'unicorn_hair': 3
    }
    total = {}
    for ingredient, amount in ingredients.items():
        total[ingredient] = amount * potions
    return total