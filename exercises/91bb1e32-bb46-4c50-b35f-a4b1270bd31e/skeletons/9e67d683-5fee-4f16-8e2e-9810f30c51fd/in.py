def sorting_hat(student_name):
    # Fill in the gaps to categorize the student
    if student_name in ['Harry', 'Hermione', 'Ron']:
        return 'Gryffindor'
    elif student_name in ['Draco', 'Pansy']:
        return 'Slytherin'
    # Add more houses here
    else:
        return 'Unknown'