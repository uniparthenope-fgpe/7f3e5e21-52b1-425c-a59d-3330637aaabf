def sorting_hat(name):
    if name[0] in 'GHJKL':
        return 'Gryffindor'
    elif name[0] in 'MNOPQ':
        return 'Hufflepuff'
    elif name[0] in 'RSTU':
        return 'Ravenclaw'
    else:
        return 'Slytherin'