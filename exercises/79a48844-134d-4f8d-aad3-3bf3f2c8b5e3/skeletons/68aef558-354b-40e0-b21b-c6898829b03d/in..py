def defensive_spell(spell):
    if spell == 'Protego':
        return 'Effective'
    elif spell == 'Expelliarmus':
        return 'Not Effective'
    return 'Unknown Spell'

print(defensive_spell('Expelliarmus'))  # Should return 'Effective'