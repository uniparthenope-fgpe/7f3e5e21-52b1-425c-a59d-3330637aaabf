def spell_checker(spell):
    known_spells = ['expelliarmus', 'avada kedavra', 'lumos']
    if spell in known_spells:
        return 'Spell is correct'
    else:
        return 'Unknown spell'