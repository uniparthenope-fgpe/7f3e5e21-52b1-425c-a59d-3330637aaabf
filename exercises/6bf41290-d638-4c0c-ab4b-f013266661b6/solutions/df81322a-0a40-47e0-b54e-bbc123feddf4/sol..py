def average_points(matches):
    total_points = 0
    for match in matches:
        total_points += match['points']
    return total_points / len(matches) if matches else 0