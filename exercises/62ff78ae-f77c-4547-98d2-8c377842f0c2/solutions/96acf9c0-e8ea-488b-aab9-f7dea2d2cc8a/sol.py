def sorting_hat(students):
    houses = {'Gryffindor': [], 'Hufflepuff': [], 'Ravenclaw': [], 'Slytherin': []}
    for student in students:
        if student[0] in 'GH':
            houses['Gryffindor'].append(student)
        elif student[0] in 'HP':
            houses['Hufflepuff'].append(student)
        elif student[0] in 'R':
            houses['Ravenclaw'].append(student)
        else:
            houses['Slytherin'].append(student)
    return houses