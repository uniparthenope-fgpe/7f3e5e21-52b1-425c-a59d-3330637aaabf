scores = {'Gryffindor': 0, 'Slytherin': 0}
for team in scores:
    scores[team] += 10
    if team == 'Gryffindor':
        scores[team] += 30  # Add bonus for catching the Snitch
print(scores)