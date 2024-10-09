def update_score(scores, team, points):
    scores[team] += points
    return scores

scores = {'Gryffindor': 0, 'Slytherin': 0}
update_score(scores, 'Gryffindor', 10)