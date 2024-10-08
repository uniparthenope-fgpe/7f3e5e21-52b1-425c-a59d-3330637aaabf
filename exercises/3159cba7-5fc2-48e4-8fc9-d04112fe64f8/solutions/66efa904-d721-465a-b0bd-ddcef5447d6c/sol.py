def sorting_hat(student_name):
    if student_name in ['Harry', 'Hermione']:
        return 'Gryffindor'
    elif student_name in ['Draco']:
        return 'Slytherin'
    elif student_name in ['Luna', 'Neville']:
        return 'Ravenclaw'
    elif student_name in ['Cedric', 'Hannah']:
        return 'Hufflepuff'
    else:
        return 'Unknown House'