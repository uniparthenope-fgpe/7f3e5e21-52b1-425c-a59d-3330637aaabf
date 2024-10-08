def select_lightsaber_color(choice):
    if choice == 'Jedi':
        return 'Green'
    elif choice == 'Sith':
        return 'Red'
    else:
        return 'Blue'

print(select_lightsaber_color('Jedi'))