def sorting_hat(preferences):
    houses = []
    for preference in preferences:
        if preference == 'bravery':
            houses.append('Gryffindor')
        elif preference == 'intelligence':
            houses.append('Ravenclaw')
        elif preference == 'loyalty':
            houses.append('Hufflepuff')
        else:
            houses.append('Slytherin')
    return houses