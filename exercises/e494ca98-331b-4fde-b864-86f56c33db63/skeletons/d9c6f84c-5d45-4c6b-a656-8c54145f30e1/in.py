def lightsaber_color(choice):
    if choice == 'Jedi':
        return 'Blue'
    elif choice == 'Sith':
        return 'Red'
    else:
        return 'Green'

# Bug: The default color should be 'Green' only for non-Jedi/Sith choices.