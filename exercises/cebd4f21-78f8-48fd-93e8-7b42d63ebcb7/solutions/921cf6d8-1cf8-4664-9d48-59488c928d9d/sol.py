def spell_checker(spell):
    correct_spells = ['Expelliarmus', 'Lumos', 'Alohomora']
    return spell in correct_spells

# Example usage:
print(spell_checker('Expelliarmus'))  # True
print(spell_checker('Avada Kedavra'))  # False