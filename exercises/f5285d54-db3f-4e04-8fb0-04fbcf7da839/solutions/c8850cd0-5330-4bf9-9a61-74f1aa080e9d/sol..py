def spell_checker(spell):
    spells = ['Expelliarmus', 'Lumos', 'Alohomora']
    if spell not in spells:
        return 'Spell not found!'
    return 'Spell is valid!'

print(spell_checker('Avada Kedavra'))