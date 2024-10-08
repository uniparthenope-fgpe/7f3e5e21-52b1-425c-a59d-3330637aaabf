def character_alignment(action):
    if action == 'help':
        return 'Jedi'
    elif action == 'destroy':
        return 'Sith'
    else:
        return 'Unknown'

# Test the function
print(character_alignment('help'))  # Output: Jedi
print(character_alignment('destroy'))  # Output: Sith
print(character_alignment('negotiate'))  # Output: Unknown