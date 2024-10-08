def sort_students(name):
    last_name = name.split()[-1]
    first_letter = last_name[0]
    # Fill in the gaps below
    if first_letter in ['A', 'B', 'C']:
        return 'Gryffindor'
    elif first_letter in ['D', 'E', 'F']:
        return 'Hufflepuff'
    elif first_letter in ['G', 'H', 'I']:
        return 'Ravenclaw'
    else:
        return 'Slytherin'