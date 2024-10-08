def protect_against_dark_arts(spell):
    if spell == 'Avada Kedavra':
        return 'Protected'
    return 'Safe'

print(protect_against_dark_arts('Avada Kedavra'))
print(protect_against_dark_arts('Expelliarmus'))