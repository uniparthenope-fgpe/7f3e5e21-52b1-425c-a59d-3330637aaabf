def sorting_hat(name):
    if name in ['Harry', 'Hermione', 'Ron']:
        return 'Gryffindor'
    elif name in ['Draco', 'Pansy']:
        return 'Slytherin'
    elif name in ['Luna', 'Neville']:
        return 'Ravenclaw'
    elif name in ['Cedric', 'Hannah']:
        return 'Hufflepuff'
    else:
        return 'Unknown'