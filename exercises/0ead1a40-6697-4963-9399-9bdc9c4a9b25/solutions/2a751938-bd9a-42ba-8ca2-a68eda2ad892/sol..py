def create_potion(ingredients):
    effectiveness = 0
    for ingredient in ingredients:
        if ingredient == 'unicorn hair':
            effectiveness += 10
        elif ingredient == 'dragon blood':
            effectiveness += 20
    return effectiveness