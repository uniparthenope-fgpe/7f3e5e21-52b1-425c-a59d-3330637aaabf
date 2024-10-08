def select_lightsaber_color(choice):
    if choice == 'Jedi':
        return 'Green'
    elif choice == 'Sith':
        return 'Red'
    else:
        return 'Blue'

# Bug: This function does not handle invalid choices properly.