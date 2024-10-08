characters = {'Harry': (4, 5), 'Ron': (3, 2), 'Hermione': (1, 4)}

def track_character(name):
    return characters.get(name, 'Character not found')

print(track_character('Harry'))