def mix_potion(ingredients):
    if 'dragon blood' in ingredients:
        return 'Elixir of Life'
    elif 'mandrake' in ingredients:
        return 'Mandrake Potion'
    elif 'potion of invisibility' in ingredients:
        return 'Invisibility Potion'
    else:
        return 'Unknown Potion'