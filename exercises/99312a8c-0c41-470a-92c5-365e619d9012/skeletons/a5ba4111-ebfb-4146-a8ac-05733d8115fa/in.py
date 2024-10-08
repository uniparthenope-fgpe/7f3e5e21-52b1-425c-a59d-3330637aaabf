def sorting_hat(students):
    gryffindor = []
    slytherin = []
    for student in students:
        # Fill in the gaps
        if student[0] < 'N':
            gryffindor.append(student)
        else:
            slytherin.append(student)
    return gryffindor, slytherin