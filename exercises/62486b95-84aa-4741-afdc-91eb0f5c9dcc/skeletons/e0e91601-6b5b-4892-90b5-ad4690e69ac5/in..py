def mix_potion(ingredients):
    total_volume = 0
    for ingredient in ingredients:
        total_volume += ingredient['volume']
    return total_volume