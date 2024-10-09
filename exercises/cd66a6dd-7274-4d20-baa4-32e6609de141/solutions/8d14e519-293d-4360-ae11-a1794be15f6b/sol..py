def cast_spell(spell_name):
    spells = {'Expelliarmus': 5, 'Stupefy': 7, 'Avada Kedavra': 10}
    return f'{spell_name} casted with power {spells.get(spell_name, 0)}!'
