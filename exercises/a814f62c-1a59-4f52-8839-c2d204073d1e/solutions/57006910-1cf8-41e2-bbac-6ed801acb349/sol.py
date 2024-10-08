def cast_spell(spell, power):
    if spell == 'Expelliarmus':
        return 'Disarming with power ' + str(power)
    elif spell == 'Stupefy':
        return 'Stunning with power ' + str(power)
    else:
        return 'Unknown spell'

print(cast_spell('Expelliarmus', 100))