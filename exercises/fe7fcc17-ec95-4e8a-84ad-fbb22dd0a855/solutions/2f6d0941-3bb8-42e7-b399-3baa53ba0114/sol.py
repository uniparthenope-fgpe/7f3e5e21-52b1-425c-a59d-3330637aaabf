def select_lightsaber_color(choice):
    if choice == 'Jedi':
        return 'Green'
    elif choice == 'Sith':
        return 'Red'
    else:
        return 'Blue'

# Added handling for invalid choices
    if choice not in ['Jedi', 'Sith']:
        return 'Invalid choice, please select Jedi or Sith.'