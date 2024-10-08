def character_alignment(action):
    if action == 'help':
        return 'Jedi'
    elif action == 'destroy':
        return 'Sith'
    else:
        return 'Unknown'

# Test the function
print(character_alignment('help'))
print(character_alignment('destroy'))
print(character_alignment('negotiate'))  # This line has a bug