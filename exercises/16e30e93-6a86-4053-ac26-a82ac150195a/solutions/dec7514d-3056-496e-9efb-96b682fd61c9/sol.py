def mix_potion(ingredients):
    potion_name = ''
    if 'unicorn hair' in ingredients and 'dragon blood' in ingredients:
        potion_name = 'Elixir of Life'
    elif 'mandrake' in ingredients:
        potion_name = 'Mandrake Draught'
    else:
        potion_name = 'Unknown Potion'
    return potion_name