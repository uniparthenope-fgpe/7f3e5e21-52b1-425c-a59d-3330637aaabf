def sort_students(students):
    houses = {'Gryffindor': [], 'Slytherin': [], 'Hufflepuff': [], 'Ravenclaw': []}
    for student in students:
        house = student['house']
        if house in houses:
            houses[house].append(student['name'])
    return houses